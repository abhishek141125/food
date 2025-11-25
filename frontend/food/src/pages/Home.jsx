import React, { useEffect, useState } from "react";
import api from "../Api";

export default function Home({ addToCart }) {
  const [foods, setFoods] = useState([]);

  useEffect(() => {
    api.get("foods/").then((res) => setFoods(res.data));
  }, []);

  return (
    <div>
      <h1>Food Menu</h1>
      <div style={{ display: "flex", gap: 20, flexWrap: "wrap" }}>
        {foods.map((food) => (
          <div key={food.id} style={{ border: "1px solid #ddd", padding: 10 }}>
            <img src={food.image} width="150" alt="" />
            <h3>{food.name}</h3>
            <p>${food.price}</p>
            <button onClick={() => addToCart(food)}>Add to Cart</button>
          </div>
        ))}
      </div>
    </div>
  );
}
