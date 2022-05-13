let std1Sec=document.getElementById("std1Sec");
       let std2Sec=document.getElementById("std2Sec");
       let std3Sec=document.getElementById("std3Sec");
       
       let std1=document.getElementById("std1");
       let std2=document.getElementById("std2");
       let std3=document.getElementById("std3");

       let stdDetails1=document.getElementById("stdDetails1");
       let stdDetails2=document.getElementById("stdDetails2");
       let stdDetails3=document.getElementById("stdDetails3");


       let stdName1=document.getElementById("stdName1");
       let stdName2=document.getElementById("stdName2");
       let stdName3=document.getElementById("stdName3");
       

       let mOver="mouseover";//mouse movements
       let mLeave="mouseleave";

       let show="block";
       let hide="none";

    //    this fuction help to code reuse ,mousehover and mouse leave two eventhandlers are 
    //      fired with one eventlistner and different times
       let mouse=(stdsec,std,stdDetails,mouseMovement,name,view)=>{
        stdsec.addEventListener(mouseMovement,()=>{
           std.style.display=view;
           stdDetails.style.display=view;
           name.style.display=view;

    });
       };
    //    calling the fuction for 6 time each 2 for one student
       mouse(std1Sec,std1,stdDetails1,mOver,stdName1,show);
       mouse(std2Sec,std2,stdDetails2,mOver,stdName2,show);
       mouse(std3Sec,std3,stdDetails3,mOver,stdName3,show);

       mouse(std1Sec,std1,stdDetails1,mLeave,stdName1,hide);
       mouse(std2Sec,std2,stdDetails2,mLeave,stdName2,hide);
       mouse(std3Sec,std3,stdDetails3,mLeave,stdName3,hide);