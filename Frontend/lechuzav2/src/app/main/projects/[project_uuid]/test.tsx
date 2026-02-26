export default function TestProjectPage({ params }: { params: { project_uuid: string } }) {
  return (
    <div className="container mx-auto py-8">
      <h1>Página de prueba para proyecto: {params.project_uuid}</h1>
      <p>Si ves esto, la ruta funciona correctamente</p>
    </div>
  )
}