import React from "react";

export function Button({ children, variant = "default", className = "", ...props }) {
  const base =
    "px-4 py-2 rounded text-sm font-medium transition focus:outline-none";
  const variants = {
    default: "bg-orange-500 text-white hover:bg-orange-600",
    outline: "border border-gray-300 text-gray-700 hover:bg-gray-100",
  };

  return (
    <button className={`${base} ${variants[variant]} ${className}`} {...props}>
      {children}
    </button>
  );
}
