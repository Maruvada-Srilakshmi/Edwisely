store = {}

def get_context(id):
    return store.get(id, {})

def update_context(id, q):
    if id not in store:
        store[id] = {}
    store[id].update({k:v for k,v in q.items() if v})