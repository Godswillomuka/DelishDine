import { useState } from "react";
import { Formik, Form, Field } from "formik";

function OrderForm() {
  const [message, setMessage] = useState("");

  return (
    <Formik
      initialValues={{ userId: "", foodItemId: "", quantity: 1 }}
      onSubmit={(values, { setSubmitting }) => {
        fetch("http://127.0.0.1:5000/api/orders", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(values),
        })
          .then((response) => response.json())
          .then((data) => {
            setMessage(data.message);
            setSubmitting(false);
          });
      }}
    >
      {({ isSubmitting }) => (
        <Form>
          <label>User ID:</label>
          <Field type="number" name="userId" required />
          <label>Food Item ID:</label>
          <Field type="number" name="foodItemId" required />
          <label>Quantity:</label>
          <Field type="number" name="quantity" required />
          <button type="submit" disabled={isSubmitting}>Place Order</button>
          {message && <p>{message}</p>}
        </Form>
      )}
    </Formik>
  );
}

export default OrderForm;
