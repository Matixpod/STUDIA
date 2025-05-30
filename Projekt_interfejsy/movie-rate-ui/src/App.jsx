import React from "react";
import { Button } from "@/components/ui/button";

export default function App() {
  return (
    <div className="font-sans text-gray-800">
      {/* Header */}
      <header className="flex justify-between items-center px-6 py-4 border-b">
        <div className="text-orange-500 font-bold text-xl">MovieRate</div>
        <nav className="space-x-4 text-sm">
          <a href="#" className="text-gray-600">TV Shows</a>
          <a href="#" className="text-gray-600">Movies</a>
          <a href="#" className="text-gray-600">Leave Review</a>
          <a href="#" className="text-gray-600">Order Review</a>
        </nav>
        <div className="space-x-2">
          <Button variant="outline">Sign In</Button>
          <Button>Sign Up</Button>
        </div>
      </header>

      {/* Hero Section */}
      <section className="relative bg-gray-200 h-[600px] flex flex-col items-center justify-center text-white text-center">
        <div className="absolute inset-0 flex items-center justify-center text-[96px] font-bold opacity-20">
          1920 × 600
        </div>
        <h1 className="text-3xl md:text-4xl font-bold z-10">Discover & Rate Your Favorite Movies</h1>
        <input
          type="text"
          placeholder="Search for movies or series..."
          className="mt-6 px-6 py-3 rounded-full shadow w-[300px] md:w-[500px] z-10"
        />
      </section>

      {/* Trending Section */}
      <section className="px-6 py-10">
        <h2 className="text-lg font-semibold mb-6">Trending Now</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
          {["The Last Chapter", "Beyond Tomorrow", "Laugh Out Loud"].map((title, idx) => (
            <div key={idx} className="bg-white p-2 rounded shadow-sm">
              <div className="bg-gray-200 h-[300px] flex items-center justify-center text-xl font-bold text-gray-400">
                400 × 600
              </div>
              <div className="mt-2">
                <div className="text-sm font-medium">{title}</div>
                <div className="text-xs text-gray-500 flex items-center space-x-2">
                  <span className="text-orange-500">⭐ 4.{idx + 4}</span>
                  <span className="bg-gray-100 px-1 rounded text-[10px]">
                    {idx === 0 ? "Drama" : idx === 1 ? "Sci-Fi" : "Comedy"}
                  </span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* About Us */}
      <section className="px-6 py-10 text-center bg-gray-50">
        <h2 className="text-lg font-semibold mb-4">About Us</h2>
        <p className="max-w-2xl mx-auto text-sm text-gray-600">
          We’re passionate about bringing you the best movie and series reviews. Our platform helps
          you discover amazing content and share your thoughts with a community of fellow
          entertainment enthusiasts.
        </p>
      </section>

      {/* Categories */}
      <section className="px-6 py-10 text-center">
        <h2 className="text-lg font-semibold mb-6">Categories</h2>
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 text-sm">
          {[
            { name: "Action", desc: "Thrilling adventures" },
            { name: "Drama", desc: "Emotional stories" },
            { name: "Comedy", desc: "Laugh out loud" },
            { name: "Sci-Fi", desc: "Future worlds" },
          ].map((cat, idx) => (
            <div key={idx} className="bg-gray-100 rounded p-4">
              <div className="font-medium">{cat.name}</div>
              <div className="text-xs text-gray-500">{cat.desc}</div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
