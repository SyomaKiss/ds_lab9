from flask import Flask, render_template, request
import pymongo

app = Flask(__name__)


client = pymongo.MongoClient('172.31.42.168', replicaSet = 'rs0')


db = client.test_database
collection = db.messages



def put(s):
    entry = {'text': s}
    collection.insert_one(entry)
    # entry = {'text': '1st message'}
    # _id = collection.insert_one(entry).inserted_id
    # entries = [{'text': '2nd message'}, {'text': '3rd message'}]
    # collection.insert_many(entries)

def get_all():
    s = ''
    l = []
    for entry in collection.find():
        # pprint(entry)
        s += entry['text']+''
        l.append(entry['text'])
    return l

print(get_all())


@app.route('/', methods=['GET', 'POST'])
def sessions():
    if request.method == 'POST':
        text = request.form.get('text')
        # print(text)
        put(text)
        # print('after: ', get_all())

    s = get_all()
    return render_template('index.html', name=s)




if __name__ == '__main__':
    # collection.delete_many({})
    app.run(host='0.0.0.0', port = 80)