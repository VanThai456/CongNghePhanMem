import json

def load_categories():
    with open("data/cate.json",encoding="utf-8") as f:
        return json.load(f)

def load_products(q=None, cate_id=None):
    with open("data/products.json",encoding="utf-8") as f:
        prods = json.load(f)

        if cate_id:
            prods = [
                p for p in prods
                if str(p["cate_id"]) == str(cate_id)
            ]

        if q:
            prods = [
                p for p in prods
                if q.lower() in p["name"].lower()
            ]

        return prods

if __name__=="__main__":
    print(load_products())