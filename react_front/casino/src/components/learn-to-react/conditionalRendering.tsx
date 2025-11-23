// function Item({ name, isPacked }) {
//   return (
//     <li className="item">
//       {name} {isPacked ? '✅': "False"}
//     </li>
//   );
// }
//
// export default function PackingList() {
//   return (
//     <section>
//       <h1>Список вещей Салли Райд</h1>
//       <ul>
//         <Item
//           isPacked={true}
//           name="Космический скафандр"
//         />
//         <Item
//           isPacked={true}
//           name="Шлем с золотым листом"
//         />
//         <Item
//           isPacked={false}
//           name="Фотография Тэма"
//         />
//       </ul>
//     </section>
//   );
// }


function Item({name, importance}) {
  return (
     <li className="item">
      {name} Importance: {importance ? importance : null}
    </li>
  );
}

export default function PackingList() {
  return (
    <section>
      <h1>Список вещей Салли Райд</h1>
      <ul>
        <Item
          isPacked={true}
          name="Космический скафандр"
        />
        <Item
          isPacked={true}
          name="Шлем с золотым листом"
          importance={"11"}
        />
        <Item
          isPacked={false}
          name="Фотография Тэма"
          importance={"12"}
        />
      </ul>
    </section>
  );
}

