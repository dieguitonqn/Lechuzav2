import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  async rewrites() {
    return [
      {
        source: "/fapi/:path*",
        destination: "http://localhost:8000/api/:path*",
        basePath: false,
      },
    ];
    },
};

export default nextConfig;
