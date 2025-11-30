import {type JSX, useState} from 'react';

//
// let initialArtists = [
//   {id: 0, name: 'Marta Colvin Andrade'},
//   {id: 1, name: 'Lamidi Olonade Fakeye'},
//   {id: 2, name: 'Louise Nevelson'},
// ];
//
//
// export default function List() {
//   const [artists, setArtists] = useState(
//     initialArtists
//   );
//
//   return (
//     <>
//       <h1>Inspiring sculptors:</h1>
//       <ul>
//         {artists.map(artist => (
//
//           <li key={artist.id}>
//             {artist.name}{' '}
//
//             <button onClick={() => {
//               setArtists(
//                 artists.filter(a =>
//                   a.id !== artist.id
//                 )
//               );
//             }}>
//               Delete
//             </button>
//
//           </li>
//         ))}
//       </ul>
//     </>
//   );
// }


// let nextId = 3;
// const initialArtists = [
//   { id: 0, name: 'Marta Colvin Andrade' },
//   { id: 1, name: 'Lamidi Olonade Fakeye'},
//   { id: 2, name: 'Louise Nevelson'},
// ];
//
// export default function List() {
//   const [name, setName] = useState('');
//   const [artists, setArtists] = useState(
//     initialArtists
//   );
//
//   function handleClick() {
//     const insertAt = 1;
//     const nextArtists = [
//       ...artists.slice(0, insertAt),
//       {id: nextId++, name: name},
//       ...artists.slice(insertAt)
//     ];
//     setArtists(nextArtists);
//     setName('');
//   }
//
//   return (
//     <>
//       <h1>Inspiring sculptors:</h1>
//       <input
//         value={name}
//         onChange={e => setName(e.target.value)}
//       />
//       <button onClick={handleClick}>
//         Insert
//       </button>
//       <ul>
//         {artists.map(artist => (
//           <li key={artist.id}>{artist.name}</li>
//         ))}
//       </ul>
//     </>
//   );
// }


// const initialProducts = [{
//   id: 0,
//   name: 'Baklava',
//   count: 1,
// }, {
//   id: 1,
//   name: 'Cheese',
//   count: 5,
// }, {
//   id: 2,
//   name: 'Spaghetti',
//   count: 2,
// }];
//
// export default function ShoppingCart() {
//   const [
//     products,
//     setProducts
//   ] = useState(initialProducts)
//
//   function handleIncreaseClick(productId) {
//     setProducts(products.map(product => {
//       if (product.id === productId) {
//         return {
//           ...product,
//           count: product.count + 1
//         };
//       } else {
//         return product;
//       }
//     }))
//   }
//
//   function handleDecreaseClick(productId) {
//     let nextProducts = products.map(product => {
//       if (product.id === productId) {
//         return {
//           ...product,
//           count: product.count - 1
//         };
//       } else {
//         return product;
//       }
//     });
//     nextProducts = nextProducts.filter(p =>
//       p.count > 0
//     );
//     setProducts(nextProducts)
//   }
//
//   return (
//     <ul>
//       {products.map(product => (
//         <li key={product.id}>
//           {product.name}
//           {' '}
//           (<b>{product.count}</b>)
//           <button onClick={() => {
//             handleIncreaseClick(product.id);
//           }}>
//             +
//           </button>
//           <button onClick={() => {
//             handleDecreaseClick(product.id);
//           }}>
//             –
//           </button>
//         </li>
//       ))}
//     </ul>
//   );
// }


import AddTodo from './addTodo.tsx';
import TaskList from './taskList.tsx';

let nextId = 3;
const initialTodos = [
  { id: 0, title: 'Buy milk', done: true },
  { id: 1, title: 'Eat tacos', done: false },
  { id: 2, title: 'Brew tea', done: false },
];

export default function TaskApp() {
  const [todos, setTodos] = useState(
    initialTodos
  );

  function handleAddTodo(title) {
    setTodos([
      ...todos,
      {
        id: nextId++,
        title: title,
        done: false
      }
    ]);
  }

  function handleChangeTodo(nextTodo) {
    setTodos(todos.map(t => {
      if (t.id === nextTodo.id) {
        return nextTodo;
      } else {
        return t;
      }
    }));
  }

  function handleDeleteTodo(todoId) {
    setTodos(
      todos.filter(t => t.id !== todoId)
    );
  }

  return (
    <>
      <AddTodo
        onAddTodo={handleAddTodo}
      />
      <TaskList
        todos={todos}
        onChangeTodo={handleChangeTodo}
        onDeleteTodo={handleDeleteTodo}
      />
    </>
  );
}

