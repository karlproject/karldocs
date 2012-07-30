========================
KARL Improvement Process
========================

The KARL project needs a way to process proposed work, through
specification, into development, and on through release and
maintenance. This "KARL Improvement Proposal" describes the improvement
process itself.

Background
==========

The KARL project has a number of actors involved: OSF as primary
driver, Six Feet Up (6FU) as a development partner, Oxfam as a
feature partner, gocept and 6FU as hosting partners, and an open source
community that is receiving KARL and doing various things that have
some consideration.

Currently, new work is discussed in various contexts, documented to
some degree, and work is commissioned by various organizations in
various ways. The work is (or isn't) specified. Work is commissioned
and tracked in one or more systems. Releases are made and some sites
are updated. Bugs are reported, for the most part,
in a single system (Launchpad.)

There isn't currently a single, one-stop-shopping place to find out
what is proposed, what is being worked on, and when something might
arrive.

Goals
=====

- Unify the various ways of doing things, by the various actors,
  into a single approach

- Provide visibility to all interested parties regarding what is
  contemplated, what is commissioned, what it will do,
  when it will arrive, and issues regarding the work

- Where possible, automate this single process with a tool

- Over time, gradually adopt this process amongst the parties

Overview
========

We want a process that spans and scales:

- Spans from "we should be doing X" all the way through "file a bug
  against X which was deployed in release Y."

- Scales from casually engaged business managers through
  deeply-involved developers and supporters, across firmly-committed
  organizations and those still evaluating

In summary:

- A *Feature* is a quick, lightweight way for business managers to
  express a need in a "Feature Backlog"

- A *Specification* is a feature that has been selected for more
  investment via analysis

- An *Initiative* is a group of features and specifications which,
  staged together, address a larger business problem.

- A *Task* is an item of development work (development, system
  administration), usually in support of a Specification or Initiative.

- A *Bug* is an item of maintenance work. Similar to,
  but not exactly the same as, a Task.

- An *Iteration* is a unit of scheduling.

- A *Release* is a unit of distribution.

- The *Roadmap* is a planning instrument showing what just happened,
  is happening, and will happen

Scenario
========

Nat and Tom are talking to OSF users during an office meeting. One of
them says "It sure would be nice to have a multiple download facility."
Nat asks: "For example?" "When I want to download all the images in a
folder, I have to visit each one, do the download, then go back to the
folder. It takes a ton of clicks!"

Nat goes to the Feature Backlog and adds a Feature. Not too many fields
on the form. Only takes 3 minutes.

Time passes.

OSF is having its iteration planning call with Paul to plan work during
the coming month. Since the Feature Backlog is the definitive source of
all that might possibly be done, the call focuses on the Feature
Backlog.

First, Nat leads an update effort, where stuff is re-prioritized. Turns
out that "Multi-File Upload" is at the top of the list. The group looks
at the KARL Roadmap, sees there is capacity in the upcoming schedule,
and decides to go for it. Paul is asked to write a Specification.

During the Partner call, OSF tells 6FU that they plan to work on
"Multi-File Upload". Calvin says "Yep, I saw that on the Feature
Backlog. We were interested in that too, glad to see it is being
commissioned. Let us know when there is a spec."

Paul goes off, writes a draft spec, gets Nat to review it. Nat makes
some comments. Paul refines, talks to some devs, gets an effort
estimate. Paul also lets the partners know that a draft spec is ready.

After a comment period, OSF says "Go!" The draft spec is a real
Specification and gets a permanent identifier (KIP-0047). The
Specification is assigned a Development Quarter of Q3 (which helps in
high-level budgeting) and a Deployment Quarter of Q3 (which helps set
user expectations.) The Feature on the Feature Backlog is archived,
making it disappear from view.

Paul, as the PM for this Specification, starts assigning Tasks. This
involves looking at the resource pool and timeline to see who is
available. The tasks are targeted to Iterations and associated with the
Specification. Paul assigns the Task to Chris as part of an Iteration.
Chris does the work for the task as part of a branch, perhaps a branch
for all work on the Specification.

When Chris finishes a Task, he marks the Task as implemented. This
makes it appear on Jim's radar as something to test. Jim does so.

As Jim and Nat do testing on the Specification, they might find Bugs,
which they file, associated with the Specification. Paul sees the new
Bug and assigns it to Carlos as part of an Iteration. Carlos fixes the
Bug, which makes it appear on Jim's radar for testing. Jim tests and
closes the bug.

At some point the Specification looks complete.