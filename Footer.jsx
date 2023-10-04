import React from "react";

export default function Footer(){
  var year = new Date().getFullYear()
  
  return(
    <div>
      <footer>
        <p>Copyright @ {year} </p>
        </footer>
    </div>
  )

}