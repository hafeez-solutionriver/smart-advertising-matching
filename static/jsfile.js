console.log("Hello buddy")



  let emb = document.getElementsByTagName("iframe")[0]
                        
  let btn = document.getElementById("adv")
  btn.addEventListener("click", myFunction);

      function myFunction(e) {
       
          
          fetch('/getfile',{
              method:"POST",
              headers : {
                'Content-Type' : "application/json"}, 
          })
          .then(response => response.json())
          .then(text => {
            console.log(text)
            const link=text.content
            console.log(link)
            emb.src=link+"?&autoplay=1"
          })
     
      }