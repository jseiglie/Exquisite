import React, { useState, useEffect } from "react";
import Employee from "../component/employee";
const Dashboard = () => {
  const [data, setData] = useState([]);
  useEffect(() => {}, []);

  return (
    <div className="d-flex align-items-start">
      <div
        className="nav flex-column nav-pills me-3"
        id="v-pills-tab"
        role="tablist"
        aria-orientation="vertical"
      >
        <button
          className="nav-link active btn-dashboard"
          id="v-pills-Employee-tab"
          data-bs-toggle="pill"
          data-bs-target="#v-pills-Employee"
          type="button"
          role="tab"
          aria-controls="v-pills-Employee"
          aria-selected="true"
        >
          Employee
        </button>
        <button
          className="nav-link btn-dashboard"
          id="v-pills-profile-tab"
          data-bs-toggle="pill"
          data-bs-target="#v-pills-profile"
          type="button"
          role="tab"
          aria-controls="v-pills-profile"
          aria-selected="false"
        >
          Profile
        </button>
        <button
          className="nav-link btn-dashboard"
          id="v-pills-disabled-tab"
          data-bs-toggle="pill"
          data-bs-target="#v-pills-disabled"
          type="button"
          role="tab"
          aria-controls="v-pills-disabled"
          aria-selected="false"
          disabled
        >
          Disabled
        </button>
        <button
          className="nav-link btn-dashboard"
          id="v-pills-messages-tab"
          data-bs-toggle="pill"
          data-bs-target="#v-pills-messages"
          type="button"
          role="tab"
          aria-controls="v-pills-messages"
          aria-selected="false"
        >
          Messages
        </button>
        <button
          className="nav-link btn-dashboard"
          id="v-pills-settings-tab"
          data-bs-toggle="pill"
          data-bs-target="#v-pills-settings"
          type="button"
          role="tab"
          aria-controls="v-pills-settings"
          aria-selected="false"
        >
          Settings
        </button>
      </div>
      <div className="tab-content w-100" id="v-pills-tabContent">
        <div
          className="tab-pane fade show active container-fluid gx-0"
          id="v-pills-Employee"
          role="tabpanel"
          aria-labelledby="v-pills-Employee-tab"
          tabIndex="0"
        >
          <Employee />
        </div>
        <div
          className="tab-pane fade"
          id="v-pills-profile"
          role="tabpanel"
          aria-labelledby="v-pills-profile-tab"
          tabIndex="0"
        >
          ...
        </div>
        <div
          className="tab-pane fade"
          id="v-pills-disabled"
          role="tabpanel"
          aria-labelledby="v-pills-disabled-tab"
          tabIndex="0"
        >
          ...
        </div>
        <div
          className="tab-pane fade"
          id="v-pills-messages"
          role="tabpanel"
          aria-labelledby="v-pills-messages-tab"
          tabIndex="0"
        >
          ...
        </div>
        <div
          className="tab-pane fade"
          id="v-pills-settings"
          role="tabpanel"
          aria-labelledby="v-pills-settings-tab"
          tabIndex="0"
        >
          ...
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
