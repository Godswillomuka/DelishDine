const styles = {
    container: {
      padding: '20px',
      maxWidth: '1200px',
      margin: '0 auto',
      fontFamily: 'Arial, sans-serif',
    },
    heading: {
      textAlign: 'center',
      fontSize: '32px',
      marginBottom: '30px',
    },
    foodItemsContainer: {
      display: 'flex',
      flexWrap: 'wrap',
      justifyContent: 'space-between',
    },
    foodItem: {
      width: '30%',
      marginBottom: '20px',
      boxSizing: 'border-box',
    },
    foodImage: {
      width: '100%',
      height: '200px',
      objectFit: 'cover',
      borderRadius: '10px',
    },
    foodName: {
      fontSize: '20px',
      marginTop: '10px',
      textAlign: 'center',
    },
    foodDescription: {
      fontSize: '14px',
      marginTop: '10px',
      textAlign: 'center',
      color: '#555',
    },
    foodPrice: {
      textAlign: 'center',
      marginTop: '10px',
      fontWeight: 'bold',
    },
    orderButton: {
      display: 'block',
      marginTop: '10px',
      padding: '10px',
      backgroundColor: '#f39c12',
      color: 'white',
      border: 'none',
      cursor: 'pointer',
      textAlign: 'center',
      borderRadius: '5px',
    },
    form: {
      marginTop: '20px',
      display: 'flex',
      flexDirection: 'column',
      width: '300px',
      margin: '0 auto',
    },
    input: {
      padding: '10px',
      marginBottom: '10px',
      fontSize: '16px',
      border: '1px solid #ddd',
      borderRadius: '5px',
    },
    submitButton: {
      padding: '10px',
      backgroundColor: '#27ae60',
      color: 'white',
      border: 'none',
      borderRadius: '5px',
      cursor: 'pointer',
    },
    orderSummary: {
      marginTop: '30px',
      padding: '20px',
      backgroundColor: '#f4f4f4',
      borderRadius: '10px',
      boxShadow: '0px 4px 8px rgba(0, 0, 0, 0.1)',
    },
    orderText: {
      fontSize: '16px',
      fontWeight: 'bold',
    },
    orderList: {
      listStyleType: 'none',
      paddingLeft: '0',
    },
    orderItem: {
      fontSize: '18px',
      margin: '10px 0',
    },
    viewOrderButton: {
      marginTop: '20px',
      padding: '10px',
      backgroundColor: '#3498db',
      color: 'white',
      border: 'none',
      borderRadius: '5px',
      cursor: 'pointer',
    },
    noOrdersText: {
      fontSize: '18px',
      color: '#888',
    },
    addNewFoodHeading: {
      textAlign: 'center',
      fontSize: '24px',
      marginTop: '40px',
    },
  };
  
  export default styles;
  