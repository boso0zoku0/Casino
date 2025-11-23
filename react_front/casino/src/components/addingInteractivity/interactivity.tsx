// export default function AppInteractivity() {
//   return (
//     <Toolbar
//       onPlayMovie={() => alert('Playing!')}
//       onUploadImage={() => alert('Uploading!')}
//     />
//   );
// }
//
// function Toolbar({ onPlayMovie, onUploadImage }) {
//   return (
//     <div>
//       <Button onClick={onPlayMovie}>
//         Play Movie
//       </Button>
//       <Button onClick={onUploadImage}>
//         Upload Image
//       </Button>
//     </div>
//   );
// }
//
// function Button({ onClick, children }) {
//
//   return (
//     <button onClick={onClick}>
//       {children}
//     </button>
//   );
// }


// function Button({ onClick, children }) {
//   return (
//     <button onClick={onClick}>
//       {children}
//     </button>
//   );
// }
//
// function PlayButton({ movieName }) {
//   function handlePlayClick() {
//     alert(`Playing ${movieName}!`);
//   }
//
//   return (
//     <Button onClick={handlePlayClick}>
//       Play "{movieName}"
//     </Button>
//   );
// }
//
// function UploadButton() {
//   return (
//     <Button onClick={() => alert('Uploading!')}>
//       Upload Image
//     </Button>
//   );
// }
//
// export default function Toolbar() {
//   return (
//     <div>
//       <PlayButton movieName="Kiki's Delivery Service" />
//       <UploadButton />
//     </div>
//   );
// }


// export default function Toolbar() {
//   return (
//     <div className="Toolbar" onClick={() => {
//       alert('You clicked on the toolbar!');
//     }}>
//       <p>wq</p>
//       <button onClick={() => alert('Playing!')}>
//         Play Movie
//       </button>
//       <button onClick={() => alert('Uploading!')}>
//         Upload Image
//       </button>
//     </div>
//   );
// }


// function Button({onClick, children}) {
//   return (
//     <button onClick={e => {
//       e.stopPropagation();
//       onClick();
//     }}>
//       {children}
//     </button>
//   );
// }
//
// export default function Toolbar() {
//   return (
//     <div className="Toolbar" onClick={() => {
//       alert('You clicked on the toolbar!');
//     }}>
//       <Button onClick={() => alert('Playing!')}>
//         Play Movie
//       </Button>
//       <Button onClick={() => alert('Uploading!')}>
//         Upload Image
//       </Button>
//     </div>
//
//   );
// }

// export default function Signup() {
//   return (
//     <form onSubmit={e =>{e.preventDefault(); alert('Q')}}>
//       <input />
//       <button>Send</button>
//     </form>
//   );
// }


// DZ

// export default function LightSwitch() {
//   function handleClick() {
//     let bodyStyle = document.body.style;
//     if (bodyStyle.backgroundColor === 'black') {
//       bodyStyle.backgroundColor = 'white';
//     } else {
//       bodyStyle.backgroundColor = 'black';
//     }
//   }
//
//   return (
//     <button onClick={handleClick}>
//       Toggle the lights
//     </button>
//   );
// }

function ButtonCollor ({onChangeColor}) {
  function handleClick () {
    document.body.style.backgroundColor = 'black'

  }

  // let changePageColor = document.body.style;
  // if (changePageColor.backgroundColor === 'black') {
  //   changePageColor.backgroundColor = 'white'
  // } else {
  //   changePageColor.backgroundColor = 'black'
  // }
}

export default function ColorSwitch({onChangeColor}) {
  return (
    <button on>
      Change color
    </button>
  );
}
