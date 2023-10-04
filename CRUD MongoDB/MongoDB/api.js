const express = require('express');
const dbConnect = require('./mongodb');
const mongodb = require('mongodb');
const app = express();
app.use(express.json());

app.get('/', async (req, res) => {
    let data = await dbConnect();
    data = await data.find().toArray();
    res.send(data);
});

app.post('/', async (req, res) => {
    let data = await dbConnect();
    let result = await data.insertOne(req.body);
    res.send(result);
    if(result.acknowledged){
        console.warn("Data posted");
    }
});

app.put('/',async (req,res)=>{
    let data = await dbConnect();
    let result = await data.updateOne(
        {name:req.body.name},
        {$set:req.body}
    );
    if(result.acknowledged){
        console.warn("data updated");
    }
});

app.delete('/', async (req, res) => {
    let data = await dbConnect();
    let result = await data.deleteOne({ _id: new mongodb.ObjectId(req.body) });
    if (result.acknowledged) {
        console.warn("data deleted");
    }
});

app.listen(2000);
