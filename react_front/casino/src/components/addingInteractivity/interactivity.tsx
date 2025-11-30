import {use, useState} from 'react';
import styles from '../../styles/interactivity.module.css';
import {useImmer} from 'use-immer'

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


// function ButtonCollor() {
//   let bodyStyle = document.body.styles;
//   function handleClick () {
//     if (bodyStyle.backgroundColor === 'black') {
//       document.body.styles.backgroundColor = 'white'
//     } else {
//       bodyStyle.backgroundColor = 'black'
//     }
//   }
//
//   return(
//     <button onClick={handleClick}>Button</button>
//   )
// }
//
// export default function ColorSwitch() {
//   return (
//     <ButtonCollor/>
//   );
// }


// const sculptureList = [{
//   name: 'Homenaje a la Neurocirugía',
//   artist: 'Marta Colvin Andrade',
//   description: 'Although Colvin is predominantly known for abstract themes that allude to pre-Hispanic symbols, this gigantic sculpture, an homage to neurosurgery, is one of her most recognizable public art pieces.',
//   url: 'https://i.imgur.com/Mx7dA2Y.jpg',
//   alt: 'A bronze statue of two crossed hands delicately holding a human brain in their fingertips.'
// }, {
//   name: 'Floralis Genérica',
//   artist: 'Eduardo Catalano',
//   description: 'This enormous (75 ft. or 23m) silver flower is located in Buenos Aires. It is designed to move, closing its petals in the evening or when strong winds blow and opening them in the morning.',
//   url: 'https://i.imgur.com/ZF6s192m.jpg',
//   alt: 'A gigantic metallic flower sculpture with reflective mirror-like petals and strong stamens.'
// }, {
//   name: 'Eternal Presence',
//   artist: 'John Woodrow Wilson',
//   description: 'Wilson was known for his preoccupation with equality, social justice, as well as the essential and spiritual qualities of humankind. This massive (7ft. or 2,13m) bronze represents what he described as "a symbolic Black presence infused with a sense of universal humanity."',
//   url: 'https://i.imgur.com/aTtVpES.jpg',
//   alt: 'The sculpture depicting a human head seems ever-present and solemn. It radiates calm and serenity.'
// }]
//
//
// export default function GalleryShow() {
//   const [index, setIndex] = useState(0);
//   const [showMore, setShowMore] = useState(false);
//
//   let hasPrev = index > 0;
//   let hasNext = index < sculptureList.length - 1;
//
//   function handlePrevClick() {
//     if (hasPrev) {
//       setIndex(index - 1);
//     }
//   }
//
//   function handleNextClick() {
//     if (hasNext) {
//       setIndex(index + 1);
//     }
//   }
//
//   function handleMoreClick() {
//     setShowMore(!showMore);
//   }
//
//   let sculpture = sculptureList[index];
//   return (
//     <>
//       <button
//         onClick={handlePrevClick}
//         disabled={!hasPrev}
//       >
//         Previous
//       </button>
//       <button
//         onClick={handleNextClick}
//         disabled={!hasNext}
//       >
//         Next
//       </button>
//       <h2>
//         <i>{sculpture.name} </i>
//         by {sculpture.artist}
//       </h2>
//       <h3>
//         ({index + 1} of {sculptureList.length})
//       </h3>
//       <button onClick={handleMoreClick}>
//         {showMore ? 'Hide' : 'Show'} details
//       </button>
//       {showMore && <p>{sculpture.description}</p>}
//       <img
//         src={sculpture.url}
//         alt={sculpture.alt}
//       />
//     </>
//   );
// }


//dz

// export default function Form() {
//   const [firstName, setFirstName] = useState('')
//   const [lastName, setLastName] = useState('')
//
//
//   function handleFirstNameChange(e) {
//     setFirstName(e.target.value);
//   }
//
//   function handleLastNameChange(e) {
//     setLastName(e.target.value);
//   }
//
//   function handleReset() {
//     setFirstName('');
//     setLastName('');
//   }
//
//   return (
//     <form onSubmit={e => e.preventDefault()}>
//       <input
//         placeholder="First name"
//         value={firstName}
//         onChange={handleFirstNameChange}
//       />
//       <input
//         placeholder="Last name"
//         value={lastName}
//         onChange={handleLastNameChange}
//       />
//       <h1>Hi, {firstName} {lastName}</h1>
//       <button onClick={handleReset}>Reset</button>
//     </form>
//   );
// }


// export default function FeedbackForm() {
//   const [message, setMessage] = useState('')
//
//   function handleClick(e) {
//     return e.target.name
//   }
//
//   if (message) {
//     return (
//       <>
//         <h2>Thank you for your comment!</h2>
//         <form onSubmit={handleClick(e)}>
//           <button onClick={handleClick} type={"submit"}>
//             Send
//           </button>
//         </form>
//       </>
//     )
//   }
// }


// export default function FeedbackForm() {
//   const [isSent, setIsSent] = useState(false);
//   if (isSent) {
//     return <h1>Thank you!</h1>;
//   } else {
//     // eslint-disable-next-line
//     const [message, setMessage] = useState('');
//     return (
//       <form onSubmit={e => {
//         e.preventDefault();
//         alert(`Sending: "${message}"`);
//         setIsSent(true);
//       }}>
//         <textarea
//           placeholder="Message"
//           value={message}
//           onChange={e => setMessage(e.target.value)}
//         />
//         <br />
//         <button type="submit">Send</button>
//       </form>
//     );
//   }
// }


// export default function MovingDot() {
//   const [position, setPosition] = useState({
//     x: 0,
//     y: 0
//   });
//   return (
//     <div
//       onPointerMove={e => {
//         setPosition({
//           x: e.clientX,
//           y: e.clientY,
//         });
//       }}
//       style={{
//         position: 'relative',
//         width: '100vw',
//         height: '100vh',
//       }}>
//       <div style={{
//         position: 'absolute',
//         backgroundColor: 'red',
//         borderRadius: '50%',
//         transform: `translate(${position.x}px, ${position.y}px)`,
//         left: -10,
//         top: -10,
//         width: 20,
//         height: 20,
//       }} />
//     </div>
//   );
// }


// export default function FormDict() {
//   const [person, setPerson] = useImmer({
//     name: 'Niki de Saint Phalle',
//     artwork: {
//       title: 'Blue Nana',
//       city: 'Hamburg',
//       image: 'https://i.imgur.com/Sd1AgUOm.jpg',
//     }
//   });
//
//   function handleNameChange(e) {
//     setPerson(draft => {
//       draft.name = e.target.value
//     })
//   }
//
//   function handleTitleChange(e) {
//     setPerson(draft => {
//       draft.artwork.title = e.target.value
//     })
//   }
//
//   function handleCityChange(e) {
//     setPerson(draft => {
//       draft.artwork.city = e.target.value
//     })
//   }
//
//   function handleImageChange(e) {
//     setPerson(draft => {
//       draft.artwork.image = e.target.value
//     })
//   }
//
//   return (
//     <>
//       <label>
//         Автор:
//         <input
//           value={person.name}
//           onChange={handleNameChange}
//         />
//       </label>
//       <label>
//         Название:
//         <input
//           value={person.artwork.title}
//           onChange={handleTitleChange}
//         />
//       </label>
//       <label>
//         Город:
//         <input
//           value={person.artwork.city}
//           onChange={handleCityChange}
//         />
//       </label>
//       <label>
//         Изображение:
//         <input
//           value={person.artwork.image}
//           onChange={handleImageChange}
//         />
//       </label>
//       <p>
//         <i>{person.artwork.title}</i>
//         {' by '}
//         {person.name}
//         <br />
//         (located in {person.artwork.city})
//       </p>
//       <img
//         src={person.artwork.image}
//         alt={person.artwork.title}
//       />
//     </>
//   );
// }


//dz


// export default function Scoreboard() {
//   const [player, setPlayer] = useState({
//     firstName: 'Ranjani',
//     lastName: 'Shettar',
//     score: 10,
//   });
//
//   function handlePlusClick() {
//     setPlayer({
//       ...player,
//       score: player.score + 1,
//     });
//   }
//
//   function handleFirstNameChange(e) {
//     setPlayer({
//       ...player,
//       firstName: e.target.value,
//     });
//   }
//
//   function handleLastNameChange(e) {
//     setPlayer({
//       ...player,
//       lastName: e.target.value
//     });
//   }
//
//   return (
//     <>
//       <label>
//         Счёт: <b>{player.score}</b>
//         {' '}
//         <button onClick={handlePlusClick}>
//           +1
//         </button>
//       </label>
//       <label>
//         Имя:
//         <input
//           value={player.firstName}
//           onChange={handleFirstNameChange}
//         />
//       </label>
//       <label>
//         Фамилия:
//         <input
//           value={player.lastName}
//           onChange={handleLastNameChange}
//         />
//       </label>
//     </>
//   );
// }