import React, { useState, useEffect } from "react";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import Cart from "./pages/Cart";

export default function App() {
  const [cart, setCart] = useState([]);

  useEffect(() => {
    const saved = localStorage.getItem("cart");
    if (saved) setCart(JSON.parse(saved));
  }, []);

  const addToCart = (food) => {
    const updated = [...cart, food];
    setCart(updated);
    localStorage.setItem("cart", JSON.stringify(updated));
  };

  return (
    <BrowserRouter>
      <nav style={{ padding: 10, borderBottom: "1px solid #ccc" }}>
        <Link to="/">Home</Link> | <Link to="/cart">Cart ({cart.length})</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home addToCart={addToCart} />} />
        <Route path="/cart" element={<Cart cart={cart} />} />
      </Routes>
    </BrowserRouter>
  );
}
