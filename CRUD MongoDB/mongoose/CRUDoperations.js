const mongoose = require('mongoose');
await mongoose.connect("mongodb://127.0.0.1:27017/e-comm");
const productSchema = new mongoose.Schema({
    name:String,
    price:Number
});

 
const saveInDB = async () =>{
    const ProductModel = mongoose.model('products',productSchema);
    let data = new ProductModel({name:'m8',price:1000, brand:'abc'});
    let result = await data.save();
    console.log("data saved");
}
saveInDB();

const updateInDB = async () =>{
    const Product = mongoose.model('products',productSchema);
    let data = await Product.updateOne(
        {name:'m8'},{
            $set:{price:700}
        }   
    );
    console.log("data updated");
}
updateInDB();

const deleteInDB = async () =>{
    const Product = mongoose.model('products',productSchema);
    let data =  await Product.deleteMany(
        {name:'test'},{price:'700'}
    );
    console.log("data deleted");
};
deleteInDB();

const findInDB = async () =>{
    const Product = mongoose.model('products',productSchema);
    let data =  await Product.find({name:'iphone14'});
    console.log(data);
    console.log("data found");
};
findInDB();