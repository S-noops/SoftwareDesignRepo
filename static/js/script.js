function fn1() {
    var total = document.getElementById("dueamount");
    var per = document.getElementById("sugprice");
    var no = document.getElementById("gallonreq");
    total.value = no.value * per.value;
}

async function fuel(){
    var gfactor = 0.03;
    var lfactor = 0.04;
    var hfactor = 0.00;
    var sug = document.getElementById("sugprice");
    var quant = document.getElementById("gallonreq").value;
    quant = parseInt(quant)

    if (quant>1000){
      gfactor = 0.02;
    }

    fetch('/getqoute', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        },
      }).then(response => {
        if (response.ok) {
          response.text().then(response => {
            response = JSON.parse(response);
            if (response.state==true){
              lfactor=0.02;
            }
            if (response.value==true){
              hfactor=0.01;
            }
            sug.value = ((lfactor - hfactor + gfactor + 0.1)*1.5) + 1.5;
            fn1()    
          });
        }
      });
}