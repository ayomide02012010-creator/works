// template string

const title = 'best reads of 2019';
const author = 'mario';
const likes = 30;

// concatenation way

let result = 'The blog called ' + title + ' by ' + author + ' has ' + likes + ' likes';
console.log(result);

// template string way 

let result = `The blog called ${title} by ${author} has ${likes} likes`;
console.log(result);

// creating html template

let html = `
<h4>${title}</h4>
<p>By ${author}</p>
<span>This blog has ${likes} likes</span
// `;
console.log(html);

let ninjas = ['shaun', 'ryu', 'chun-li' ];
ninjas[1] = 'ken';
console.log(ninjas[1]);