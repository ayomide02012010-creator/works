// // // let email = "aliabdulrasaq69@gmail.com";

// // // // let result = email.lastIndexOf('l');
// // // // let resut = email.slice(3,9);

// // // // let result = email.substring(3,9);
// // // let result = email.replace('d', "h");
// // // console.log(result);



// // let radius = 10;
// // const pi = 3.14;

// // // console.log(10 / 2);

// // // let result = radius % 3;
// //  // let result = radius**2 * pi;
// // // order of operation - B I D M A S

// // // let result = 10 * (20-6)**2;
// // // console.log(result);

// // let likes = 20;

// // // likes = likes + 6;
// // // likes -= 10;
// // // likes *= 3
// // // console.log(likes);
// // console.log(5 * 'hello');

// // let result = 'The blog has ' +  likes + " likes";
// // console.log(result);

// // // // string

// // // console.log('hello, world');

// // // let email = 'aliabdulrasaq69@gmail.com';
// // // console.log(email);

// // // var firstName = "Ibrahim";
// // // const secondName = "Yusuf";
// // // const thirdName = 'Olatunji';

// // // let fullName = firstName + ' ' + secondName + ' ' + thirdName;

// // // console.log(fullName);
// // // console.log(fullName[0]);
// // // console.log(fullName.length);
// // // console.log(fullName.toUpperCase());

// // // let result = fullName.toLowerCase();
// // // console.log(result, fullName);

// // // let index = email.indexOf('@');
// // // console.log(index);

// const title = "Best reads of 2019";
// const author = "mario";
// const likes = 30;

// // CONCATENATION WAY
// // let result = 'The blog called ' + title + ' by ' + author + " has " + likes + ' likes'
// // console.log(result);

// // TEMPLATE STRING WAY
// let result = `The blog called ${title} by ${author} has ${likes} likes `
// console.log(result);

// // CREATING HTML TEMPLATE
// let html = `
//    <h2>${title}</h2>
//    <p> By ${author}</p>
//    <span>This blog has ${likes} likes</span>

// `;
// console.log(html);
let names = ["Ali",'Ayomide','bt-bs'];

// names[1] = "tom";
// console.log(names[1]);

// let age = [20,25,28,29];
// console.log(age[2]);

// let random = ["shaun", 67, 'raj', '56', 90, 't'];
// console.log(random);

// console.log(names.length);

// Array methoD

// let result = names.join('-');
// let result = names.indexOf("bt-bs");
// let result = names.concat(['ibrahim', 'uthman']);
// let result = names.push('ibrahim');
// console.log(result);
// console.log(names[3]);

// console.log("JavaScript loaded!");
// for(let i = 5; i <= 13; i++){
//     console.log("in loop", i);
      
// }
// console.log("loop finished");

const names = ['shaun', 'mario', 'luigi'];

let i = 0;
while(i < names.length){ 
    console.log(names[i]);
    i++;
}
