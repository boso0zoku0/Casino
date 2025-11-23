

function Profile({person, pictures, profession, awards, discovered}) {
  return (
    <div>
      <h1>{person}</h1>
      <img src={pictures} alt={"photoOne"}/>
      <ul>
        <li>
          Profession: {profession}
        </li>
        <li>
          Awards: {awards}
        </li>
        <li>
          Discovered: {discovered}
        </li>
        <li>
          if (isTrue) {
          <li>"True"</li>
        }
          <li>False</li>
        </li>
      </ul>
    </div>
  )
}



export default function Profiles() {
  return (
    <>
      <Profile person={"Jack"}
               pictures={"https://static.vecteezy.com/system/resources/thumbnails/045/132/934/small/a-beautiful-picture-of-the-eiffel-tower-in-paris-the-capital-of-france-with-a-wonderful-background-in-wonderful-natural-colors-photo.jpg"}
               profession={"It"}
               awards={"(Nobel Prize in Physics, Nobel Prize in Chemistry, Davy Medal, Matteucci Medal)"}
               discovered={"polonium (chemical element)"}

      />
      <hr/>


      <Profile person={"Bob"}
               pictures={"https://media.licdn.com/dms/image/v2/D5612AQE8NiooxTxA3w/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1695825196046?e=2147483647&v=beta&t=2zU71mKLxGihkNQB5eMDjCgbD7srasN1gyEqowXMGV4"}
               profession={"It"}
               awards={"(Bob in Physics, Bob in Chemistry, Davy Medal, Matteucci Medal)"}
               discovered={"polonium (chemical element)"}
      />
    </>
  )
}


