var total_gas=0;
var total_elec=0;

var elec_list=[];

window.addEventListener('DOMContentLoaded', function() {
    console.log("laoded");

    
    

    
   



    
})

function change(){
    document.getElementById("total_gas").innerHTML=`ガス総使用量：${total_gas}`;
    document.getElementById("total_elec").innerHTML=`電力総使用量：${total_elec}`;
    
    for(let i=0;i<5;i++){
        console.log(`elec${i}`);
        document.getElementById(`elec${i+1}`).innerHTML=elec_list[i];
    }
}
function test(){
    total_gas=300
    total_elec=500
    elec_list=["冷蔵庫：使用量：50%：円","エアコン：使用量：25%：使用円","電子レンジ：使用量：15%：使用円","ドライヤー：使用量：6%：使用円","掃除機：使用量：4%：使用円"];
    change();
    helloApi();
}

//restAPI
async function callApi() {
    for(let i=0;i<5;i++){
        let res = await fetch(`http://127.0.0.1:8000/wat_${i}`)
            .then(result => result.json())
            .then((output) => {
                console.log('Output: ', output);
                let wat_full = output["full"];
                let wat_per = output["per"];
                let wat_yen = output["yen"];
                let wat_name= output["name"];
                elec_list[i]=wat_name+"　使用量："+wat_full+"kwh　使用%："+"%　使用円："+wat_yen+"円"
                console.log( String(tmpVal) );
            }).catch(err => console.error(err));
    }
  };

  async function helloApi() {
    for(let i=0;i<5;i++){
        let res = await fetch(`http://localhost:8080/api/wat_full`)
            .then(result => result.json())
            .then((output) => {
                console.log('Output: ', output);
                let wat_full = output["Hello"];
                console.log( String(wat_full) );
            }).catch(err => console.error(err));
    }
  };