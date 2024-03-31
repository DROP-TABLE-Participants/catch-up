<template>
    <div class="navbar">
    <div class="navbar__logo">
        <router-link to="/" class="navbar__logo">
            <img src="../assets/logo.png" alt="logo"/>
        </router-link>
    </div>
    <div class="navbar__links">
      <router-link to="/pricing">Pricing</router-link>
      <router-link to="/dashboard">Dashboard</router-link>
      <router-link to="/test">Try it out</router-link>
    </div>
    <div class="navbar__button">
      <router-link to="/login">Login</router-link>
    </div>
  </div>
    <div class="pricing-page">
      <div class="pricing-card">
        <h2>Basic</h2>
        <div class="price">25$/month</div>
        <ul>
          <li>0-80 products</li>
          <li>Full Functionality</li>
        </ul>
      </div>
  
      <div class="pricing-card recommended">
        <h2>Pro</h2>
        <div class="price">75$/month</div>
        <ul>
          <li>80-200 products</li>
          <li>Full Functionality</li>
          <li>Personalized emails every week</li>
        </ul>
      </div>
  
      <div class="pricing-card">
        <h2>Premium</h2>
        <div class="price">150$/month</div>
        <ul>
          <li>200-500 products</li>
          <li>Full Functionality</li>
          <li>Personalized emails every week</li>
          <li>24/7 Technical Support</li>
          <li>Priority Support</li>
        </ul>
      </div>
    </div>
  </template>
  
  <style scoped lang="scss">
  * {
  font-family: 'Hanken Grotesk', sans-serif;
    }

.navbar {
  display: flex;
  justify-content: space-around;
  align-items: center;
  position: relative;
  width: 100vw;
  margin-top: 40px;

  &__logo {
    img {
      width: 130px;
    }
  }

  &__links {
    display: flex;
    gap: 2rem;

    a {
      text-decoration: none;
      color: #000;
      font-weight: 500;

      &:hover {
        text-decoration: underline;
      }
    }
  }

  &__button {
    a {
      padding: 0.5rem 1rem;
      background-color: #00E99E;
      color: #262626;
      border-radius: 5px;
      width: 40px;
      text-decoration: none;
      transition: background-color 0.3s;

      &:hover {
        background-color: #3bf0b7;
      }
    }
  }
}

  .pricing-page {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    margin-top: 200px;
  }
  
  .pricing-card {
    width: 300px;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    text-align: center;
  }
  
  .pricing-card h2 {
    font-size: 24px;
    color: #333;
  }
  
  .price {
    font-size: 36px;
    font-weight: bold;
    color: #007bff;
    margin-bottom: 20px;
  }
  
  ul {
    list-style: none;
    padding: 0;
  }
  
  ul li {
    margin-bottom: 10px;
  }
  
  button {
    padding: 10px 20px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  
  .recommended {
    border-color: #007bff;
    box-shadow: 0px 0px 10px 0px rgba(0, 123, 255, 0.3);
  }
  
  @media (max-width: 768px) {
    .pricing-page {
      flex-direction: column;
    }
  
    .pricing-card {
      width: 100%;
    }
  }
  </style>
  