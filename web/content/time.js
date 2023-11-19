var total_gas=0;
var total_elec=0;
var elec_other=0;
var time;//朝0昼1晩2
var now = new Date();
var justnow;

var  elec_list= new Array(6); //要素数5の配列(array)を作成
for(let y = 0; y < 6; y++) {
  elec_list[y] = new Array(2).fill(0); //配列(array)の各要素に対して、要素数5の配列を作成し、0で初期化
}

window.addEventListener('DOMContentLoaded', function() {
    console.log("laoded");

    
    

    if(document.getElementById("asa") != null){
        time=0;
    }else if(document.getElementById("hiru") != null){
        time=1;
    }else if(document.getElementById("yoru") != null){
        time=2;
    }
    
    change();
})


function LoadProc() {
  
  var Hour = now.getHours();
  var Min = now.getMinutes();
  justnow="更新日時："+Hour+":"+Min;
  document.getElementsByClassName("update_time").innerHTML=justnow;
}




function change(){
    console.log("change");
    document.getElementById("total_gas").innerHTML=total_gas;
    document.getElementById("total_elec").innerHTML=total_elec;
    document.getElementById("other").innerHTML=elec_other;
    
    for(let i=1;i<=5;i++){
        console.log(`elec${i}`);
        document.getElementById(`elec${i}`).innerHTML=elec_list[i][1];
    }
    LoadProc();
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
    let res_gas_full = await fetch(`http://localhost:8080/api/gas_total_hour${time}`,{
            method: "POST"
        })
            .then(result => result.json())
            .then((output) => {
                console.log('Output: ', output);
                let gas_full = output["amount"];
                let gas_per  = output["rate"];
                total_gas="ガス使用割合："+gas_full+"m³："+gas_per+"%";
                console.log(total_gas);
            }).catch(err => console.error(err));
    let res_elec_full = await fetch(`http://localhost:8080/api/elec_total_hour${time}`,{
            method: "POST"
        })
            .then(result => result.json())
            .then((output) => {
                console.log('Output: ', output);
                let wat_full = output["amount"];
                let wat_per = output["rate"];
                total_elec="電力使用割合："+wat_full+"kWh："+wat_per+"%";
                console.log(total_elec);
            }).catch(err => console.error(err));

    for(let i=1;i<=5;i++){
        let res_elec_item = await fetch(`http://localhost:8080/api/elec_hour${time}_wat_${i}`,{
            method: "POST"
        })
            .then(result => result.json())
            .then((output) => {
                console.log('Output: ', output);
                let wat_full = output["full"];
                let wat_per = output["per"];
                let wat_yen = output["yen"];
                let wat_name= output["name"];
                elec_list[i][0]=wat_full;
                elec_list[i][1]=wat_name+"："+wat_full+"kwh："+wat_per+"%："+wat_yen+"円";
                console.log( elec_list[i][1] );
            }).catch(err => console.error(err));
            
    }

    elec_list.sort(function(a,b){return(b[0] - a[0]);});//sort

    let res_elec_other = await fetch(`http://localhost:8080/api/elec_hour${time}_other`,{
            method: "POST"
        })
            .then(result => result.json())
            .then((output) => {
                console.log('Output: ', output);
                let wat_full = output["full"];
                let wat_per = output["per"];
                let wat_yen = output["yen"];
                let wat_name= output["name"];
                elec_other=wat_name+"："+wat_full+"kwh："+wat_per+"%："+wat_yen+"円";
                console.log(elec_other);
            }).catch(err => console.error(err));
    change();
  };


  

