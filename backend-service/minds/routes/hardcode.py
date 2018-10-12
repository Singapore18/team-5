# import logging

from flask import request, jsonify

from minds import application as app
from minds import db

# logger = logging.getLogger(__name__)
@app.route('/user/<user_id>', methods=['GET'])
def get_user_data(user_id):
    result = db.get(user_id)
    return jsonify(result)

@app.route('/user/<user_id>/shopping/add/list/<list_id>', methods=['GET'])
def add_to_shopping(user_id, list_id):
    # TODO
    result = db.get(user_id)
    return jsonify({"status":"api not working"})
    return jsonify(result)

@app.route('/user/<user_id>/list', methods=['GET'])
def get_user_all_list(user_id):
    result = db.get(user_id)['lists']
    return jsonify(result)


@app.route('/user/<user_id>/list/<list_id>', methods=['GET'])
def get_user_list(user_id, list_id):
    result = db.get(user_id)['lists']
    if list_id in result:
        result = result[list_id]
    else:
        result = {
            "items": []
        }
    return jsonify(result)


def calculate_price(items):
    price = 0
    for item in items:
        price += item['qty']*item['price']
    return price


@app.route('/user/<user_id>/list/<list_id>/add/<item_id>', methods=['GET'])
def add_item_to_list(user_id, list_id, item_id):
    data = db.get(user_id)
    result = data['lists']
    if list_id in result:
        if int(item_id) in mapping:
            item = mapping[int(item_id)]
        else:
            return jsonify({"error": "item not found"})
        added = False
        for i in range(len(data['lists'][list_id]['items'])):
            if data['lists'][list_id]['items'][i]['id'] == int(item_id):
                data['lists'][list_id]['items'][i]['qty'] += 1
                added = True
                break
        if not added:
            item['qty'] = 1
            data['lists'][list_id]['items'].append(item)
        db.update(user_id, data)
        result = {"status": "item added"}
    else:
        return jsonify({"error": "list not found"})

    return jsonify(result)


@app.route('/user/<user_id>/list/<list_id>/delete/<item_id>', methods=['GET'])
def remove_item_from_list(user_id, list_id, item_id):
    data = db.get(user_id)
    result = data['lists']
    if list_id in result:
        if int(item_id) in mapping:
            # item = mapping[int(item_id)]
            pass
        else:
            return jsonify({"error": "item not found"})
        added = False
        for i in range(len(data['lists'][list_id]['items'])):
            if data['lists'][list_id]['items'][i]['id'] == int(item_id):
                if data['lists'][list_id]['items'][i]['qty'] == 1:
                    del data['lists'][list_id]['items'][i]
                else:
                    data['lists'][list_id]['items'][i]['qty'] -= 1
                added = True
                break
        if not added:
            return jsonify({"error": "item not in list"})
        db.update(user_id, data)
        result = {"status": "item removed"}
    else:
        return jsonify({"error": "list not found"})

    return jsonify(result)


@app.route('/catalogue', methods=['GET'])
def get_catalogue():
    return jsonify(all_item)


@app.route('/catalogue/<category>', methods=['GET'])
def get_catalogue_by_cat(category):
    if category in catalogue:
        result = catalogue[category]
    else:
        result = []
    return jsonify(result)
    # result = {"items": catalogue[category]}
    # return jsonify(result)


@app.route('/hardcode', methods=['GET'])
def hardcode():
    # data = request.get_json()
    # app.logger.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input")
    # result = inputValue * inputValue
    # app.logger.info("My result :{}".format(result))

    response = {
        "items": [
            {
                "id": 1,
                "name": "jelly",
                "qty": 2,
                "price": 9.54
            }, {
                "id": 2,
                "name": "peanut",
                "qty": 1,
                "price": 15.24
            }, {
                "id": 3,
                "name": "shampoo",
                "qty": 3,
                "price": 1.00
            }, {
                "id": 4,
                "name": "spam",
                "qty": 1,
                "price": 0.25
            }
        ]
    }
    return jsonify(response)
    # return jsonify(result)


@app.route('/hardcode2', methods=['GET'])
def hardcode2():
    response = [
        {
            "id": 1,
            "name": "jelly",
            "qty": 2,
            "price": 9.54
        }, {
            "id": 2,
            "name": "peanut",
            "qty": 1,
            "price": 15.24
        }, {
            "id": 3,
            "name": "shampoo",
            "qty": 3,
            "price": 1.00
        }, {
            "id": 4,
            "name": "spam",
            "qty": 1,
            "price": 0.25
        }
    ]

    return jsonify(response)


@app.route('/item/<item_id>', methods=['GET'])
def get_item(item_id):

    items = {
        '0001': {
            "id": 1,
            "name": "jelly",
            "price": 9.54,
            "description": "wobbly wobbly wobbly wobbly wobbly ",
            "country": "China",
            "supplier": "CHINA NUMBA wan",
            "rating": "4.2/5 (451 ratings)",
            "serial": "54651598453",
            "image": "http://blog.partypieces.co.uk/wp-content/uploads/2015/01/jan-2015-pineapplejelly.jpg"
        },
        '0002': {
            "id": 2,
            "name": "peanut",
            "price": 15.24,
            "description": "wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly ",
            "country": "China",
            "supplier": "CHINA NUMBA wan",
            "rating": "4.2/5 (451 ratings)",
            "serial": "54651598453",
            "image": "https://www.sciencenews.org/sites/default/files/styles/growth_curve_main/public/2017/01/main/blogposts/011317_MR_peanut-allergies_main.jpg?itok=c8zS79Sb"
        },
        '0003': {
            "id": 3,
            "name": "shampoo",
            "price": 1.00,
            "description": "wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly ",
            "country": "China",
            "supplier": "CHINA NUMBA wan",
            "rating": "4.2/5 (451 ratings)",
            "serial": "54651598453",
            "image": "https://images-na.ssl-images-amazon.com/images/I/716GPlRZ23L._SL1500_.jpg"
        },
        '0004': {
            "id": 4,
            "name": "spam",
            "price": 0.25,
            "description": "wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly wobbly ",
            "country": "China",
            "supplier": "CHINA NUMBA wan",
            "rating": "4.2/5 (451 ratings)",
            "serial": "54651598453",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Spam_can.png/220px-Spam_can.png"
        }
    }

    response = items[item_id]
    return jsonify(response)


meat = [
    {
        "id": 11,
        "name": "Kee Song Chicken - Kampong",
        "weight": "900g",
        "price": 7.40,
        "country": "Malaysia",
        "description": "Fresh chicken parts. Freshness guaranteed. Estimated product life for 3 days including delivery day.",
        "url": "https://s3-ap-southeast-1.amazonaws.com/www8.fairprice.com.sg/fpol/media/images/product/XL/13132878_XL1.jpg"
    },
    {
        "id": 12,
        "name": "Australia Pork - Minced",
        "weight": "300g",
        "price": 4.10,
        "country": "Australia",
        "description": "Fresh pork direct flown from Australia.",
        "url": "https://s3-ap-southeast-1.amazonaws.com/www8.fairprice.com.sg/fpol/media/images/product/XL/13132878_XL1.jpg"
    },
    {
        "id": 13,
        "name": "Meatlovers Tochigi Wagyu A4 Steak",
        "weight": "200g",
        "price": 57.70,
        "country": "Japan",
        "description": "Steak sliced from A4 grade wagyu. Our Tochigi Wagyu is on par with many famous Japanese beef brands. Deriving from pure lineage, these black haired cattles are raised only by designated commercial farmers passing strict requirements. Smooth and marbled meat with rich flavor.",
        "url": "https://s3-ap-southeast-1.amazonaws.com/media.redmart.com/newmedia/1600x/i/m/2000005002007_0094_1455666654471.jpg"
    }
]
vegetable = [
    {
        "id": 21,
        "name": "Pasar Xiao Bai Chye",
        "weight": "220g",
        "price": 0.80,
        "country": "Singapore",
        "description": "Store at room temperature.",
        "url": "https://s3-ap-southeast-1.amazonaws.com/www8.fairprice.com.sg/fpol/media/images/product/XL/13032618_XL1.jpg"
    },
    {
        "id": 22,
        "name": "Sakura Pearl Brinjal",
        "weight": "300g",
        "price": 1.40,
        "country": "Malaysia",
        "description": "No pesticide. No chemical fertiliser. Advanced Japanese lacto farming technology. Tasty and nutritious.",
        "url": "https://s3-ap-southeast-1.amazonaws.com/www8.fairprice.com.sg/fpol/media/images/product/XL/12605904_XL1.jpg"
    },
    {
        "id": 23,
        "name": "Pasar Prepacked Carrots",
        "weight": "500g",
        "price": 0.90,
        "country": "Australia",
        "description": "The Australian carrots are extremely crunchy and are a rich source of vitamin A and antioxidant agents.",
        "url": "https://s3-ap-southeast-1.amazonaws.com/www8.fairprice.com.sg/fpol/media/images/product/XL/13000321_XL1.jpg"
    }
]
fruit = [
    {
        "id": 31,
        "name": "Apple Fiesta New Zealand Apple Bag - Royal Gala",
        "weight": "1.3kg",
        "price": 5.90,
        "country": "New Zealand",
        "description": "The fruit is two toned with a orange red blush that is commonly striped. The fruit also has sweet yellowish flesh and a crisp texture. The fruit is rich in fibre, antioxidants, vitamin C, A, potassium and iron.",
        "url": "https://s3-ap-southeast-1.amazonaws.com/www8.fairprice.com.sg/fpol/media/images/product/XL/13099853_XL1.jpg"
    },
    {
        "id": 32,
        "name": "Pasar Hong Kong Papaya",
        "weight": "1.6kg",
        "price": 2.90,
        "country": "Malaysia",
        "description": "The papaya has a red orange and yellow flesh that is soft to the touch. Its flesh is firm, juicy, aromatic and has a buttery sweetness. It has anti-inflammatory properties and contains Vitamin A and C. It can be used as garnish to make dishes attractive, added to fruit salads or blended with peanut butter for a tasty spread.",
        "url": "https://s3-ap-southeast-1.amazonaws.com/www8.fairprice.com.sg/fpol/media/images/product/XL/13004610_XL1.jpg"
    },
    {
        "id": 33,
        "name": "Sunkist Delite Australian Mandarins",
        "weight": "600g",
        "price": 4.60,
        "country": "Australia",
        "description": "he fruit's exterior has a beautiful, bright and bumpy rind. Their sparkling orange interior is exceptionally sweet.",
        "url": "https://s3-ap-southeast-1.amazonaws.com/www8.fairprice.com.sg/fpol/media/images/product/XL/13052577_XL1.jpg"
    }
]
dairy = []
carb = []
drink = []


catalogue = {
    "meat": meat,
    "vegetable": vegetable,
    "dairy": dairy,
    "drink": drink,
    "fruit": fruit,
    "carb": carb
}

all_item = []
for items in catalogue:
    all_item += catalogue[items]
mapping = {}
for item in all_item:
    mapping[item["id"]] = item
