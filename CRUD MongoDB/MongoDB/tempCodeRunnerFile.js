
app.put('/',async(req, res)=>{
    let data= await dbConnect();
    console.log(req.body.name);
    let result= data.updateOne(
        {name:req.body.name},
        {$set:req.body}
    )
});