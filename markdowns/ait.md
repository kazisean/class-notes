---
mainfont: "Helvetica Neue"
sansfont: "Helvetica Neue"
monofont: "Menlo"

header-includes:
  - \usepackage{amssymb}
---

\newpage
# Indroduction + How to use guide 








\newpage 
### Todo 
```
[ ] Lecture #11
[ ] Lecture #14
[ ] Lecture #15
[ ] Lecture #16
[ ] Lecture #17
[ ] Lecture #18

[ ] Lecture #19 (in class exam)
[ ] Lecture #20
[ ] Lecture #21
[ ] Lecture #22
[ ] Lecture #23
[ ] Lecture #24
[ ] Lecture #25
```




## Lecture 19 : Ajax




### Practice Questions
1. Create and implement a generic XMLHttpRequest object. 
```js
const req = new XMLHttpRequest();
req.open('GET', url, true); // request method, url (string), asynchronous (boolean)
req.addEventListener('load') {..} // on load
req.addEventListener('error') {..} // on errror
req.send(); // to send out your request. If post send takes in data as arg
```

A Quick Example
Using this json file:

request the file from a blank page
parse the JSON… and insert each object's message into document.body as a div

Some setup to serve this exercise, as well as a few others: →

1. setup a barebones express app
2. create the json file above in your public folder
3. create an html file called hello.html in your public folder
4. set up some boilerplate html
5. just add script tags to include the following
6. create a JavaScript file called hello.js in your public/javascripts folder



### Anki
What is traditional web application?
-> The application itself is mostly server-sided, the client side is usually just presentation. Where after posting or getting some information from the backend the client side loads another page or refresh current page. 

What is single page web application?
-> In this type of application only a single page is loaded. Content is added to pages as necessary wihtout reloading the page or transferring control to another page. 


How does single page web application work?
-> While on a page, the user can trigger background requests to the server, in this case the server returns data rather than html document. The client is updated when the data is get or posted. 

What does Ajax stands for?
-> Asynchronous JavasScript and XML(can be json or anything else even html fragments)


What is XMLHttpRequest?
-> It is JS object that allows browser based JS to make http requests. 

How does XMLHttpRequest work?
-> First create an XMLHttpRequest object, next configure it with the right request method and url, next specify what should it do on error and content load, send out the request. 

What is the code needed to get the click action of the following 
```html
<input type="button" id="get-messages-button" value="GET MAH MSGS">?
```
-> 
```js 
const button = document.getElementByID('get-messages-button');
button.addEventListener('click', function (e) {
  ....
})

```


XHR sucess block
```js
if (x.status >= 200 && x.staus <= 400 ){
  const data = JSON.parse(x.responseText);
}
```
Fetch write block

```js
const res = await fetch ('https://api.com/get/asda', {
  method: 'POST'
  headers: {
    'Content-Type' = 'application/json'
  },
  body: JSON.stringify({text})
})
```
promise fetched data
```js
const data = await fetch(url).then(r => r.json())
```


Rest API example


```js
router.get('/api/messages', async (req, res ) => {
  const msgs = await Messages.find();
  res.json(msgs);
})

router.post('/api/messages', async (req, res) => {
  const msgs = await Message.create({text: req.body.text, date: Date.now()});
  res.status(201).json({id:msgs._id})
})

```















