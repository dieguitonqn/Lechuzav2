import React, { use } from 'react'
import { auth } from "@/auth"


export default async function Main() {
const session = await auth();

  return (
    <div>
      Holas
    </div>
  )
}
