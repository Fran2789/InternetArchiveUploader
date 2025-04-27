from internetarchive import get_item
item = get_item('<unique_item_identifier>')
for k,v in item.metadata.items():
    print(print(k,":",v))