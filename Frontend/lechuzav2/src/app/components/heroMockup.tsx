import React from "react";
interface HeroMockupProps {
  isVisible: boolean;
}

export default function HeroMockup({ isVisible }: HeroMockupProps) {
    return (
        <div>
             {/* Hero Image/Mockup */}
            <div className={`transition-all duration-1000 delay-300 ${isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'}`}>
              <div className="relative">
                <div className="bg-white rounded-2xl shadow-2xl p-6 transform rotate-2 hover:rotate-0 transition-transform duration-300">
                  <div className="bg-gradient-to-br from-slate-500 to-slate-600 rounded-lg p-8 text-white">
                    <div className="flex items-center justify-between mb-6">
                      <h3 className="text-xl font-semibold">Dashboard Principal</h3>
                      <div className="flex space-x-2">
                        <div className="w-3 h-3 bg-red-400 rounded-full"></div>
                        <div className="w-3 h-3 bg-yellow-400 rounded-full"></div>
                        <div className="w-3 h-3 bg-green-400 rounded-full"></div>
                      </div>
                    </div>
                    <div className="space-y-4">
                      <div className="bg-white/20 rounded-lg p-4">
                        <div className="flex items-center justify-between">
                          <span>Proyectos Activos</span>
                          <span className="font-bold">24</span>
                        </div>
                      </div>
                      <div className="bg-white/20 rounded-lg p-4">
                        <div className="flex items-center justify-between">
                          <span>Documentos Procesados</span>
                          <span className="font-bold">1,247</span>
                        </div>
                      </div>
                      <div className="bg-white/20 rounded-lg p-4">
                        <div className="flex items-center justify-between">
                          <span>Usuarios Activos</span>
                          <span className="font-bold">156</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

        </div>
    )
}