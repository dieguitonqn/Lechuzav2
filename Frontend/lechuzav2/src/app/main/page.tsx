import React, { use } from 'react'
import { auth } from "@/auth"


export default async function Main() {
const session = await auth();

const list_projects = await fetch("localhost:8000/api/v1/projects/projects", {
  method: "GET",
  headers: {
    
    "Authorization": `Bearer ${session?.accessToken}`,
  },
})

console.log("🚀 Session in Main page:", session);

console.log("🚀 Fetching projects with access token:", session?.accessToken);

console.log("🚀 Fetch response:", list_projects);

  return (
    <div>
      Holas
    </div>
  )
}
