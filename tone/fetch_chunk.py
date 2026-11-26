"""Fetch own Substack posts, split into passages. Raw text goes ONLY to the scratch dir (arg 1).
Repo keeps passages_index.csv: id, date, post slug, hash, word count. No text."""
import csv,sys,json,re,time,hashlib,html,urllib.request,os
scratch=sys.argv[1]; H={"User-Agent":"Mozilla/5.0"}
def strip(h):
    h=re.sub(r"<(script|style)[\s\S]*?</\1>","",h)
    h=re.sub(r"</(p|h\d|li|blockquote|div)>","\n\n",h); h=re.sub(r"<br\s*/?>","\n",h)
    return html.unescape(re.sub(r"<[^>]+>","",h))
idx=[]; texts={}
for r in csv.DictReader(open("posts.csv")):
    u=f"https://adventurecapital.substack.com/api/v1/posts/{r['slug']}"
    try: d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=30))
    except Exception as e: print("skip",r["slug"],e); continue
    body=strip(d.get("body_html") or "")
    paras=[p.strip() for p in body.split("\n\n") if len(p.split())>=8]
    # merge paragraphs into ~150-250 word passages
    cur=[];n=0;k=0
    for p in paras+[None]:
        if p is None or n>=150:
            if cur and n>=60:
                t=" ".join(cur); pid=f"{r['date']}_{r['slug'][:20]}_{k}"; k+=1
                texts[pid]=t; idx.append((pid,r["date"],r["slug"],hashlib.sha256(t.encode()).hexdigest()[:12],len(t.split())))
            cur=[];n=0
        if p: cur.append(p); n+=len(p.split())
    time.sleep(1.5)
with open("passages_index.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["id","date","slug","hash","words"]); w.writerows(idx)
json.dump(texts,open(os.path.join(scratch,"passages.json"),"w"))
print(len(idx),"passages from",len({i[2] for i in idx}),"posts;",sum(i[4] for i in idx),"words")
