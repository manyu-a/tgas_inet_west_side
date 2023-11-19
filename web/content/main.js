var total_gas=0;
var total_elec=0;


var elec_list=[];

window.addEventListener('DOMContentLoaded', function() {
    console.log("laoded");

    
    setInterval(callApi,5000);

    
   



    
})

function change(){
    console.log("change");
    document.getElementById("total_gas").innerHTML=total_gas;
    document.getElementById("total_elec").innerHTML=total_elec;
    
    
    for(let i=1;i<=5;i++){
        console.log(`elec${i}`);
        document.getElementById(`elec${i}`).innerHTML=elec_list[i];
    }
}
function test(){
    // total_gas=300
    // total_elec=500
    // elec_list=["冷蔵庫：50%：4000円","エアコン：25%：3000円","電子レンジ：15%：使用円","ドライヤー：使用量：6%：使用円","掃除機：使用量：4%：使用円"];
    console.log("callApi");
    callApi();
}

//restAPI
async function callApi() {
    console.log("callApi");
    let res_gas_full = await fetch(`http://localhost:8080/api/gas_full`,{
            method: "POST"
        })
            .then(result => result.json())
            .then((output) => {
                console.log('Output: ', output);
                let gas_full = output["full"];
                let gas_yen  = output["yen"];
                total_gas="ガス総使用量："+gas_full+"m³："+gas_yen+"円";
                console.log(total_gas);
            }).catch(err => console.error(err));
    let res_elec_full = await fetch(`http://localhost:8080/api/wat_full`,{
            method: "POST"
        })
            .then(result => result.json())
            .then((output) => {
                console.log('Output: ', output);
                let wat_full = output["full"];
                let wat_yen = output["yen"];
                total_elec="電力総使用量："+wat_full+"kWh："+wat_yen+"円";
                console.log(total_elec);
            }).catch(err => console.error(err));

    for(let i=1;i<=5;i++){
        let res_elec_item = await fetch(`http://localhost:8080/api/wat_${i}`,{
            method: "POST"
        })
            .then(result => result.json())
            .then((output) => {
                console.log('Output: ', output);
                let wat_full = output["full"];
                let wat_per = output["per"];
                let wat_yen = output["yen"];
                let wat_name= output["name"];
                elec_list[i]=wat_name+"："+wat_full+"kwh："+wat_per+"%："+wat_yen+"円";
                console.log( elec_list[i] );
            }).catch(err => console.error(err));
    }
    change();
  };


  
