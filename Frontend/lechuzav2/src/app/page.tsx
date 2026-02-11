'use client'
import { useState, useEffect } from "react";
import { signIn } from "next-auth/react";
import Image from "next/image";
import {
  ArrowRight,
  FileText,
  Users,
  BarChart3,
  Shield,
  Clock,
  CheckCircle,
  Play,
  Monitor,
  Smartphone,
  Cloud,
  Star,
  Menu,
  X
} from "lucide-react";
import HeroMockup from "./components/heroMockup";

export default function Home() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  const features = [
    {
      icon: <FileText className="w-8 h-8 text-red-500" />,
      title: "Gestión de Documentos",
      description: "Administra y controla todos los documentos de tus proyectos de manera centralizada y segura."
    },
    {
      icon: <Users className="w-8 h-8 text-red-500" />,
      title: "Colaboración en Equipo",
      description: "Facilita la colaboración entre equipos con herramientas de comunicación y seguimiento integradas."
    },
    {
      icon: <BarChart3 className="w-8 h-8 text-red-500" />,
      title: "Reportes y Analytics",
      description: "Genera reportes detallados y obtén insights valiosos sobre el progreso de tus proyectos."
    },
    {
      icon: <Shield className="w-8 h-8 text-red-500" />,
      title: "Seguridad Avanzada",
      description: "Protege tu información con los más altos estándares de seguridad y control de acceso."
    }
  ];

  const stats = [
    { number: "15+", label: "Proyectos Gestionados" },
    { number: "13+", label: "Empresas Confían" },
    { number: "99.9%", label: "Uptime Garantizado" },
    { number: "24/7", label: "Soporte Técnico" }
  ];

  return (
    <div className="min-h-screen bg-white">
      {/* Navigation */}
      <nav className="bg-white/95 backdrop-blur-md border-b border-gray-200 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">

            <div className="flex items-center">
              <div>
                <Image
                  src={"/lechu_logo_new.jpg"}
                  alt="EPEN Logo"
                  width={50}
                  height={50}
                  className="mr-3"
                />
              </div>
              <div className="text-2xl font-bold text-red-600">LechuzaV2</div>
              <div className="ml-2 text-sm text-gray-500 hidden sm:block">Sistema de Gestión</div>
            </div>

            {/* Desktop Navigation */}
            <div className="hidden md:flex items-center space-x-8">
              <a href="#features" className="text-gray-700 hover:text-slate-600 transition-colors">
                Características
              </a>
              <a href="#demo" className="text-gray-700 hover:text-slate-600 transition-colors">
                Demo
              </a>
              <a href="#contact" className="text-gray-700 hover:text-slate-600 transition-colors">
                Contacto
              </a>
              <div className="flex items-center space-x-3">
                <button
                  onClick={() => signIn()}
                  className="text-gray-700 hover:text-red-600 transition-colors"
                >
                  Iniciar Sesión
                </button>
                <button
                  onClick={() => signIn()}
                  className="bg-red-600 text-white px-4 py-2 rounded-lg hover:bg-red-700 transition-colors"
                >
                  Registrarse
                </button>
              </div>
            </div>

            {/* Mobile menu button */}
            <div className="md:hidden">
              <button
                onClick={() => setIsMenuOpen(!isMenuOpen)}
                className="text-gray-700 hover:text-red-600 focus:outline-none"
              >
                {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
              </button>
            </div>
          </div>
        </div>

        {/* Mobile Navigation */}
        {isMenuOpen && (
          <div className="md:hidden bg-white border-t border-gray-200">
            <div className="px-4 pt-2 pb-3 space-y-1">
              <a href="#features" className="block px-3 py-2 text-gray-700 hover:text-red-600">
                Características
              </a>
              <a href="#demo" className="block px-3 py-2 text-gray-700 hover:text-red-600">
                Demo
              </a>
              <a href="#contact" className="block px-3 py-2 text-gray-700 hover:text-red-600">
                Contacto
              </a>
              <div className="flex flex-col space-y-2 px-3 pt-2">
                <button
                  onClick={() => signIn()}
                  className="text-left text-gray-700 hover:text-red-600"
                >
                  Iniciar Sesión
                </button>
                <button
                  onClick={() => signIn()}
                  className="bg-red-600/70 text-white px-4 py-2 rounded-lg hover:bg-red-700 transition-colors text-center"
                >
                  Registrarse
                </button>
              </div>
            </div>
          </div>
        )}
      </nav>

      {/* Hero Section */}
      <section className="relative bg-gradient-to-br from-gray-50 via-white to-slate-50 overflow-hidden">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div className={`transition-all duration-1000 ${isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'}`}>
              <h1 className="text-5xl lg:text-6xl font-bold text-gray-900 leading-tight mb-6">
                Gestiona tus
                <span className="text-red-600"> proyectos</span>
                <br />con inteligencia
              </h1>
              <p className="text-xl text-gray-600 mb-8 leading-relaxed">
                LechuzaV2 es la plataforma integral que revoluciona la gestión de documentos
                y proyectos. Controla, colabora y optimiza cada aspecto de tu flujo de trabajo.
              </p>
              <div className="flex flex-col sm:flex-row gap-4">
                <button
                  onClick={() => signIn()}
                  className="bg-red-600/70 text-white px-8 py-4 rounded-lg text-lg font-medium hover:bg-red-700 transition-colors flex items-center justify-center group"
                >
                  Comenzar ahora
                  <ArrowRight className="ml-2 w-5 h-5 group-hover:translate-x-1 transition-transform" />
                </button>
                <button className="border border-gray-300 text-gray-700 px-8 py-4 rounded-lg text-lg font-medium hover:bg-gray-50 transition-colors flex items-center justify-center">
                  <Play className="mr-2 w-5 h-5" />
                  Ver Demo
                </button>
              </div>
            </div>
            <HeroMockup isVisible={isVisible} />
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="bg-slate-600 text-white py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-2 lg:grid-cols-4 gap-8">
            {stats.map((stat, index) => (
              <div key={index} className="text-center">
                <div className="text-4xl lg:text-5xl font-bold mb-2">{stat.number}</div>
                <div className="text-slate-200">{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-24 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">
              Características Principales
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Descubre todas las herramientas que necesitas para optimizar
              la gestión de tus proyectos y documentos.
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {features.map((feature, index) => (
              <div
                key={index}
                className="bg-white rounded-xl p-6 shadow-lg hover:shadow-xl transition-shadow duration-300 group"
              >
                <div className="mb-4 group-hover:scale-110 transition-transform duration-300">
                  {feature.icon}
                </div>
                <h3 className="text-xl font-semibold text-gray-900 mb-3">
                  {feature.title}
                </h3>
                <p className="text-gray-600">
                  {feature.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Demo Section */}
      <section id="demo" className="py-24">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 mb-4">
              Ve LechuzaV2 en Acción
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Explora las principales funcionalidades de nuestra plataforma
            </p>
          </div>

          <div className="grid lg:grid-cols-3 gap-8">
            {/* Feature Screenshots */}
            <div className="bg-white rounded-2xl shadow-xl overflow-hidden">
              <div className="bg-gradient-to-r from-slate-400 to-slate-500 h-48 flex items-center justify-center">
                <Monitor className="w-16 h-16 text-white" />
              </div>
              <div className="p-6">
                <h3 className="text-xl font-semibold mb-3">Dashboard Intuitivo</h3>
                <p className="text-gray-600">
                  Interfaz limpia y moderna que te permite visualizar toda la información importante de un vistazo.
                </p>
              </div>
            </div>

            <div className="bg-white rounded-2xl shadow-xl overflow-hidden">
              <div className="bg-gradient-to-r from-purple-400 to-pink-500 h-48 flex items-center justify-center">
                <Smartphone className="w-16 h-16 text-white" />
              </div>
              <div className="p-6">
                <h3 className="text-xl font-semibold mb-3">Acceso Móvil</h3>
                <p className="text-gray-600">
                  Gestiona tus proyectos desde cualquier dispositivo con nuestra aplicación web responsive.
                </p>
              </div>
            </div>

            <div className="bg-white rounded-2xl shadow-xl overflow-hidden">
              <div className="bg-gradient-to-r from-yellow-400 to-orange-500 h-48 flex items-center justify-center">
                <Cloud className="w-16 h-16 text-white" />
              </div>
              <div className="p-6">
                <h3 className="text-xl font-semibold mb-3">En la Nube</h3>
                <p className="text-gray-600">
                  Almacenamiento seguro en la nube con acceso desde cualquier lugar y respaldo automático.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="bg-gradient-to-r from-slate-600 to-slate-700 text-white py-24">
        <div className="max-w-4xl mx-auto text-center px-4 sm:px-6 lg:px-8">
          <h2 className="text-4xl font-bold mb-6">
            ¿Listo para revolucionar tu gestión de proyectos?
          </h2>
          <p className="text-xl text-slate-200 mb-8">
            Únete a las empresas que ya confían en LechuzaV2 para optimizar sus procesos
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <button
              onClick={() => signIn()}
              className="bg-white text-slate-700 px-8 py-4 rounded-lg text-lg font-medium hover:bg-gray-100 transition-colors flex items-center justify-center group"
            >
              Comenzar gratis
              <ArrowRight className="ml-2 w-5 h-5 group-hover:translate-x-1 transition-transform" />
            </button>
            <button className="border border-white text-white px-8 py-4 rounded-lg text-lg font-medium hover:bg-white/10 transition-colors">
              Solicitar Demo
            </button>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-4 gap-8">
            <div className="col-span-2">
              <div className="text-2xl font-bold text-slate-400 mb-4">LechuzaV2</div>
              <p className="text-gray-400 mb-4 max-w-md">
                La plataforma integral para la gestión eficiente de proyectos y documentos.
              </p>
              <div className="flex space-x-4">
                {[1, 2, 3, 4, 5].map((star) => (
                  <Star key={star} className="w-5 h-5 text-yellow-400 fill-current" />
                ))}
                <span className="text-gray-400 ml-2">4.9/5</span>
              </div>
            </div>

            <div>
              <h3 className="text-lg font-semibold mb-4">Producto</h3>
              <ul className="space-y-2 text-gray-400">
                <li><a href="#" className="hover:text-white transition-colors">Características</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Precios</a></li>
                <li><a href="#" className="hover:text-white transition-colors">API</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Documentación</a></li>
              </ul>
            </div>

            <div>
              <h3 className="text-lg font-semibold mb-4">Soporte</h3>
              <ul className="space-y-2 text-gray-400">
                <li><a href="#" className="hover:text-white transition-colors">Centro de Ayuda</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Contacto</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Estado del Sistema</a></li>
                <li><a href="#" className="hover:text-white transition-colors">Actualizaciones</a></li>
              </ul>
            </div>
          </div>

          <div className="border-t border-gray-800 mt-12 pt-8 flex flex-col md:flex-row justify-between items-center">
            <p className="text-gray-400">© 2026 LechuzaV2. Todos los derechos reservados.</p>
            <div className="flex space-x-6 mt-4 md:mt-0">
              <a href="#" className="text-gray-400 hover:text-white transition-colors">Privacidad</a>
              <a href="#" className="text-gray-400 hover:text-white transition-colors">Términos</a>
              <a href="#" className="text-gray-400 hover:text-white transition-colors">Cookies</a>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}
