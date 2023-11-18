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
    elec_list=["冷蔵庫：使用料：50%：円","エアコン：使用料：25%：使用円","電子レンジ：使用料：15%：使用円","ドライヤー：使用料：6%：使用円","掃除機：使用料：4%：使用円"];
    change();
}