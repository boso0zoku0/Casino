import React from 'react';
// import {all} from "axios";



const baseUrl = 'https://i.imgur.com/';
const person = {
  name: 'Gregorio Y. Zara',
  imageId: '7vQD0fP',
  imageSize: 's',
  theme: {
    backgroundColor: 'black',
    color: 'pink'
  }
};

const allUrl = baseUrl + person.imageId + person.imageSize + '.jpg'

export default function TodoList() {
  return (
    <div style={person.theme}>
      <h1>{person.name}'s Todos</h1>
      <img
        className="avatar"
        src={allUrl}
        alt={person.name}
      />
      <ul>
        <li>Improve the videophone</li>
        <li>Prepare aeronautics lectures</li>
        <li>Work on the alcohol-fuelled engine</li>
      </ul>
    </div>
  );
}


















// const today = new Date();
//
// function formatDate(date) {
//   return new Intl.DateTimeFormat(
//     'en-US',
//     { weekday: 'short',
//       month: 'short',
//       day: 'numeric'
//     }
//   ).format(date);
// }
//
//
// export default function ShowTime() {
//   return (
//     <h2>Time {formatDate(today)}</h2>
//   )
// }