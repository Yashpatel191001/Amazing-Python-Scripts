const express = require('express');
const Product = require('./product');
const mongoose = require('mongoose');
require('./config');
const app = express();
app.use(express.json());

app.post("/create",async (req,res)=>{
    res.send('hello');
    let data = new Product(req.body);
    let result = await data.save();
    console.warn(result);
});

app.get("/list", async(req, res)=>{
    let data = await Product.find();
    res.send(data);
});

app.delete("/delete/:id", async (req,res)=>{
    let data = await Product.deleteOne({ _id: req.params.id});
    res.send('done');
});

app.put("/update/:_id", async(req,res)=>{
    let data = await Product.updateOne(
        {name:req.body.name},
        {
            $set:req.body
        }
    );
    res.send('updated');
});

app.listen(9000);