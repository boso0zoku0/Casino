import {Fragment, useState} from 'react';

// const peopleList = [
//   'Креола Кэтрин Джонсон (Creola Katherine Johnson): математик',
//   'Марио Молина (Mario José Molina-Pasquel Henríquez): химик',
//   'Мухаммад Абдус Салам (Mohammad Abdus Salam): физик',
//   'Перси Джулиан (Percy Lavon Julian): химик',
//   'Субраманьян Чандрасекар (Subrahmanyan Chandrasekhar): астрофизик'
// ];
//
//
// export default function PeopleList() {
//   const listPeople = peopleList.filter(person => <li>{person}</li>)
//   return (
//     <ul>
//       {listPeople}
//     </ul>
//   )
// }


// const people = [{
//   id: 0,
//   name: 'Креола Кэтрин Джонсон (Creola Katherine Johnson)',
//   profession: 'математик',
// }, {
//   id: 1,
//   name: 'Марио Молина (Mario José Molina-Pasquel Henríquez)',
//   profession: 'химик',
// }, {
//   id: 2,
//   name: 'Мухаммад Абдус Салам (Mohammad Abdus Salam)',
//   profession: 'физик',
// }, {
//   id: 3,
//   name: 'Перси Джулиан (Percy Lavon Julian)',
//   profession: 'химик',
// }, {
//   id: 4,
//   name: 'Субраманьян Чандрасекар (Subrahmanyan Chandrasekhar)',
//   profession: 'астрофизик',
// }];

// export default function PeopleList() {
//   const chemists = people.filter(person =>
//     person.profession === 'химик'
//   );
//   const listItems = chemists.map(person =>
//     <Fragment key={person.id}>
//       {person.profession}
//     </Fragment>
//   );
//   return (
//     <ul>
//       {listItems}
//     </ul>
//   )}


// export default function List() {
//   const listFilter = people.filter(person => person.profession === "химик")
//   const chemists = listFilter.map(person =>
//     <li key={person.id}>
//       <img
//         src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvPwuxBhcP25ZMoQ8MI6Ip-F6mDXlI8bDo2w&s"
//         alt={person.name}
//       />
//       <p>
//         <b>{person.name}:</b>
//         {' ' + person.profession}
//       </p>
//     </li>
//   );
//   const excludeChemists = people.filter(person => person.profession != "химик")
//   const showExclude = excludeChemists.map(person => <li key={person.id}>{person.name}:{person.profession}</li>)
//   return (
//     <article>
//       <h1>Ученые химики</h1>
//       <ul>{chemists}</ul>
//       <h1>Остальные ученые</h1>
//       <ul>{showExclude}</ul>
//     </article>
//   );
// }


export const recipes = [{
  id: 'greek-salad',
  name: 'Греческий салат',
  ingredients: ['помидоры', 'огурец', 'лук', 'оливки', 'сыр фета']
}, {
  id: 'hawaiian-pizza',
  name: 'Гавайская пицца',
  ingredients: ['тесто для пиццы', 'соус для пиццы', 'моцарелла', 'ветчина', 'ананас']
}, {
  id: 'hummus',
  name: 'Хумус',
  ingredients: ['нут', 'оливковое масло', 'зубчики чеснока', 'лимон', 'тахини']
}];


// export default function RecipeList() {
//   return (
//     <div>
//       <h1>Рецепты</h1>
//       {recipes.map(recipe =>
//         <div key={recipe.id}>
//           <h2>{recipe.name}</h2>
//           <ul>
//             {recipe.ingredients.map(ingredient =>
//               <li key={ingredient}>
//                 {ingredient}
//               </li>
//             )}
//           </ul>
//         </div>
//       )}
//     </div>
//   );
// }


// function Recipe({ id, name, ingredients }) {
//   return (
//     <div>
//       <h2>{name}</h2>
//       <ul>
//         {ingredients.map(ingredient =>
//           <li key={ingredient}>
//             {ingredient}
//           </li>
//         )}
//       </ul>
//     </div>
//   );
// }
//
// export default function RecipeList() {
//   return (
//     <div>
//       <h1>Рецепты</h1>
//       {recipes.map(recipe =>
//         <Recipe {...recipe} key={recipe.id} />
//       )}
//     </div>
//   );
// }


// const poem = {
//   lines: [
//     'Я пишу, стираю, переписываю,',
//     'Снова стереть, а затем',
//     'Цветет мак.'
//   ]
// };
//
// export default function Poem() {
//   let output = [];
//
//   poem.lines.forEach((line, index) => {
//       output.push(
//         <hr key={index + '-separator'}/>
//       )
//       output.push(
//         <p key={index + '-text'}>{line}</p>
//       )
//     }
//   )
//   return (
//     <article>
//       {output}
//     </article>
//   )
// }


// let guest = 0;
//
// function Cup({guest}) {
//   // Bad: changing a preexisting variable!
//   return <h2>Tea cup for guest #{guest}</h2>;
// }
//
// export default function TeaSet() {
//   return (
//     <>
//       <Cup guest={2}/>
//     </>
//   );
// }

// dz

// export default function Clock() {
//   let time = new Date
//   let hours = time.getHours();
//   let className;
//   if (hours >= 0 && hours <= 6) {
//     className = 'night';
//   } else {
//     className = 'day';
//   }
//   return (
//     <h1 className={className}>
//       {time.toLocaleTimeString()}
//     </h1>
//   );
// }


// dz

export default function StoryTray({ stories }) {
  const [state, setState] = useState(false)
  function handleClick() {
    window.location.href = 'https://web.telegram.org/k/#@gigachat_bot'
  }

  return (
    <ul>
      {stories.map(story => (
        <li key={story.id} onClick={() => setState(true)}>
          Label-{story.label} ID-{story.id}
        </li>
      ))}
      {state &&
      <button type={"submit"} onClick={handleClick}>Create story</button>}
    </ul>
  );
}
