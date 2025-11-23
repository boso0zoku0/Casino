import {useState} from "react";


type Status = true | false

export default function Gallery() {
  const [state, setState] = useState<Status>(true)

  const toggleState = () => {
    setState(setState => setState)
  }


  return (
    <>
      <button onClick={toggleState}>Click {state}</button>
      <Profile isActive={toggleState}/>
    </>
  )
}

// ✅ Определяйте компоненты на верхнем уровне
function Profile({isActive}) {
  return (
    <div>I'm User {isActive ? "active" : "unactive"}</div>
  )
}

