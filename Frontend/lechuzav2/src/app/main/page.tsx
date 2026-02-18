import React from 'react'
import { auth } from "@/auth"
import { Project } from './interfaces';
import ProjectCards from './components/project_cards';
import { redirect } from 'next/navigation';

export default async function Main() {
  const session = await auth();
  
  if (!session?.accessToken) {
    redirect("/auth/signin");
  }
  
  let body: Project[] = [];
  try {
    const list_projects = await fetch("http://localhost:8000/api/v1/projects/", {
      method: "GET",
      headers: {
        "Authorization": `Bearer ${session.accessToken}`,
        "Content-Type": "application/json",
      },
    })

    if (list_projects.status === 401) {
      console.log("Token inválido o expirado. Redirigiendo a login...");
      redirect("/auth/signout");
    }
    body = await list_projects.json();
  } catch (error) {
    console.log("Error fetching projects:", error);
    redirect("/auth/signout");
  }


  console.log("🚀 Session in Main page:", session);

  console.log("🚀 Fetching projects with access token:", session?.accessToken);

  console.log("🚀 Fetch response:", body);

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-2">
            Mis Proyectos
          </h1>
          <p className="text-gray-600">
            Gestiona y visualiza todos tus proyectos en un solo lugar
          </p>
        </div>

        {/* Project Cards */}
        <ProjectCards projects={body} isAdmin={session?.user?.role === "admin"} />
      </div>
    </div>
  )
}

