export default function TakePictures() {

interface PhotoData {
    src: string;
    height: string;
    weight: string
}

const photoData: PhotoData = {
    src: "https://i.pinimg.com/originals/16/e0/4d/16e04de6654613c3ea72c7f3ad8eca2a.jpg",
    height: "100px",
    weight: "100px"
};

  function handleClick() {
    alert("KU")
  }


  return <img src={photoData.src} alt="Кэтрин Джонсон" onClick={handleClick} height={photoData.height} width={photoData.weight}/>;
}
