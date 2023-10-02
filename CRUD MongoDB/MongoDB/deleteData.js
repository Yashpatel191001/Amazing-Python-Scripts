const dbConnect = require('./mongodb');

const deleteData = async () =>{
    let data =await dbConnect();
    let result = data.deleteOne({name:'nord3'});
    console.log('record deleated');
}
deleteData();