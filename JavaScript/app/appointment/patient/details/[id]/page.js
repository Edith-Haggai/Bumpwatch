"use client";
import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import Header from "@/components/layout/Header";

export default function AppointmentDetailsPage() {
  const { id } = useParams();
  const [userDetails, setUserDetails] = useState(null);

  useEffect(() => {
    if (id) {
      fetch(`/api/profile?_id=${id}`).then((response) => {
        response.json().then((data) => {
          setUserDetails(data);
          console.log(data);
        });
      });
    }
  }, [id]);

  if (!userDetails) {
    return "Loading...";
  }

  return (
    <>
      <Header color={"bg-gradient-to-r from-pink-700 via-purple-700 to-indigo-700"} />
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-r from-pink-100 via-purple-100 to-indigo-100 p-4">
        <div className="max-w-5xl bg-white shadow-lg rounded-lg p-8 mx-4 mt-24 mb-20 w-full">
          <h1 className="text-4xl font-bold text-gray-800 mb-6 text-center">User Details</h1>

          <div className="space-y-8">
            <div className="bg-gray-50 p-6 rounded-lg shadow-inner">
              <h2 className="text-2xl font-semibold mb-4">Profile Information</h2>
              <div className="space-y-4">
                <p className="text-lg"><strong>Name:</strong> {userDetails?.name}</p>
                <p className="text-lg"><strong>Email:</strong> {userDetails?.email}</p>
                <p className="text-lg"><strong>Profile Created:</strong> {userDetails.createdAppointment ? "Yes" : "No"}</p>
                <p className="text-lg"><strong>Date of Birth:</strong> {userDetails.DOB ? new Date(userDetails.DOB).toLocaleDateString() : "N/A"}</p>
                <p className="text-lg"><strong>Phone:</strong> {userDetails.phone || "N/A"}</p>
                <p className="text-lg"><strong>Country:</strong> {userDetails.country || "N/A"}</p>
                <p className="text-lg"><strong>Gender:</strong> {userDetails.gender || "N/A"}</p>
                <p className="text-lg"><strong>Due Date:</strong> {userDetails.dueDate ? new Date(userDetails.dueDate).toLocaleDateString() : "N/A"}</p>
                <p className="text-lg"><strong>Weeks:</strong> {userDetails.weeks || "N/A"}</p>
                <p className="text-lg"><strong>Children:</strong> {userDetails.children || "N/A"}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
