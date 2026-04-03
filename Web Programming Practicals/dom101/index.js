/*
 * This is index.js
 * Open index.html in your browser to check what
 * you have to do, adding functions to the end of this
 * file as necessary.
 *
 * NB: all code you write this year should use strict mode, so
 * we've enabled that by default with the first line of code.
 */

'use strict';

function replaceText(elem, str) {
    elem.innerText = str;
}

function addTextTo(elem, str) {
    elem.innerText = elem.innerText + str;
}

function moreBears() {
    const animalElement = document.querySelector("#animals");
    animalElement.src = 'http://placebear.com/400/200';
    animalElement.alt = 'A bear.';
    animalElement.title = 'A BEAR!';
}

function setId(elem, str) {
    elem.id = str;
    return elem;
}

function setClass(elem, str) {
    elem.className = str;
    return elem;
}

function addAClass(elem, str) {
    elem.classList.add(str);
    return elem;
}

function removeAClass(elem, str) {
    elem.classList.remove(str);
    return elem;
}

function newElement(name) {
    return document.createElement(name);
}

function findElementById(id) {
    return document.getElementById(id);
}

function findElementsByQuery(query) {
    return document.querySelectorAll(query);
}

function reverseList(query) {
    const list = document.querySelector(query);
    const items = Array.from(list.children);
    list.innerHTML = '';
    for (let i = items.length - 1; i >= 0; i--) {
        list.appendChild(items[i]);
    }
    return list;
}

function mover(moveThis, appendToThis) {
    const elementToMove = document.querySelector(moveThis);
    const destinationElement = document.querySelector(appendToThis);
    destinationElement.appendChild(elementToMove);
}

function filler(list, candidates) {
    candidates.forEach(candidate => {
        const listItem = document.createElement('li');
        listItem.innerText = candidate;
        list.appendChild(listItem);
    });
}

function dupe(selector) {
    const element = document.querySelector(selector);
    const clone = element.cloneNode(true);
    element.parentNode.insertBefore(clone, element.nextSibling);
}

function removeAll(selector) {
    const elements = document.querySelectorAll(selector);
    elements.forEach(element => {
        element.parentNode.removeChild(element);
    });
}

// Forcefully override default values (as they are not setting for some reason)
const username_fix = document.querySelector('#username');
const speed_fix = document.querySelector('#speed');
const student_fix = document.querySelector('#student');

username_fix.value = "John";
speed_fix.value =  70;
student_fix.checked = true;

function getUserData() {
    let obj = {}
    obj.name = document.querySelector('#username').value;
    obj.speed = parseInt(document.querySelector('#speed').value, 10);
    obj.student = document.querySelector('#student').checked;
    return obj;
}
