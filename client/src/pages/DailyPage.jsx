import { useLoaderData } from "react-router-dom"
import DailyCard from "../components/DailyCard.jsx"

function DailyPage() {
  const postureData = useLoaderData();
  
  return (
  <>
    <DailyCard data={postureData}/>          
    </>
  )
}

export default DailyPage