"""Word-list baseline. Reads passages from a scratch JSON (arg 1); prints/saves per-year rates only."""
import json,re,sys,csv,collections
t=json.load(open(sys.argv[1]))
L={"moral":"should must ought wrong evil shame disgrace obviously clearly simply refuse fail failure fools idiots stupid blame dishonest lazy unacceptable".split(),
   "hedge":"maybe perhaps might probably possibly seems guess unsure tradeoff however though but depends roughly honestly".split(),
   "first_person":"i i'm i've my me".split()}
agg=collections.defaultdict(lambda:collections.Counter())
for pid,x in t.items():
    y=pid[:4]; w=re.findall(r"[a-z']+",x.lower()); agg[y]["n"]+=len(w)
    for k,l in L.items(): agg[y][k]+=sum(c in l for c in w)
with open("wordlist_by_year.csv","w",newline="") as f:
    wr=csv.writer(f); wr.writerow(["year","words"]+[f"{k}_per1k" for k in L])
    for y in sorted(agg):
        r=[y,agg[y]["n"]]+[round(1000*agg[y][k]/agg[y]["n"],1) for k in L]; wr.writerow(r); print(r)
