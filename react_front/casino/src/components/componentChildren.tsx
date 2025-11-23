function ComponentOne({children}) {
  return (
    <>
      <h1>Hello, I'm first function</h1>
      <img src="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/13/f8/5c/05/picture-lake.jpg?w=1200&h=-1&s=1"
           alt={"Dw"}/>
      <div>
        {children}
      </div>
    </>
  )
}


export default function ComponentTwo() {
  const yearDate = new Date().getFullYear().toString()
  return (
    <>
      <h3>I'm a two function</h3>
      <ComponentOne>
        <ComponentThree/>
      </ComponentOne>
    </>
  )
}

function ComponentThree() {
  return (
    <>
      <h3>I'm a two fweqf</h3>
      <img
        src="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1b/01/bd/a3/see-two-for-the-price.jpg?w=900&h=500&s=1"
        alt={"Dw"}/>
    </>
  )

}