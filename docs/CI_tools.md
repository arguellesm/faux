# CI tool selection

## Criteria

Criteria from more to less important:

- **Price.** The selected tool should be free to use or at 
least have a free tier option, preferably with no need of 
sharing our credit card information.
- **Hosting.** It should offer a cloud-based option as we
don't have the resources to deploy it on-premise.
- **GitHub integration.** It should be easy to integrate with
GitHub.
- **Difficulty.** The selected tool shouldn't require a 
high level of expertise to be installed, configured or used.
- **Feature set.** This is not a requirement itself, as all
CI tools will have the minimun features to work properly, but
extra features and fine-tuned options are welcome assuming 
previous requirements are met. 


## Search and options

A Google search for CI tools gave us some of the following
alternatives:

- AWS CI
- Travis CI
- TeamCity
- GoCD
- Jenkins
- Bamboo CI
- GitLab CI/CD
- CodeShip
- Semaphore CI
- GitHub Actions
- Buddy

Circle CI did also appeared in the search but we didn't 
include it as an option as most projects already used it.


## Comparisons and elimination

We'll be going through each of the criterion listed above 
to compare our alternatives and discard those that not meet 
the criteria.

### Price

Except CodeShip, all of them offer at least one free plan 
that varies a bit in credits, storage or minutes a month. 
Both Travis CI and AWS CI have a free plan, but they 
require a credit card when signin up. 

We'll be discarding CodeShip for not being free and Travis
CI and AWS CI for requiring billing information. 

Price is discussed again at the end of this section focusing
on how cost-effective each option is. The reason not to do 
it now is to avoid analysing tools that might be rejected 
inmediatly after due to other major requirements like cloud 
hosting or GitHub integration.

### Hosting

The following tools need to be self-hosted: GoCD (needs
server and agent), Jenkins and Bamboo. We won't be 
considering any of those because of this reasons.

### GitHub integration

All of them can easly work along GitHub, although GitHub 
actions is the most tightly integrated one for obvious 
reasons.

### Difficulty

We checked the documentation and getting started guides 
of each options to get an idea of how they work, and we also
signed up for the free plan on all of them to play around.
While checking them out, GitLab's and Buddy's interface were 
the less intuitive and harder to navigate than those of 
GitHub and Semaphore CI. 

Other than that, hey all seemed more or less similar 
and well-suited to our level of expertise.

### Price (cost-effectiveness)

At this point we were left with the following alternatives:

- TeamCity
- GitLab CI/CD
- Semaphore CI
- Buddy
- GitHub Actions

To futher compare these options will be discussing whether 
they can be long-term or not and the features they have.

TeamCity and Buddy free plans are advertised as that but
are rather free trials that expire within 14 days. Because 
we expect to keep using whatever CI tool we choose, these
are obviously not a good pick.

As for the features of the remaning plans:

| Tool           | Minutes | Package storage |
|----------------|---------|-----------------|
| GitLab CI/CD   | 400     | 5GB             |
| Semaphore CI   | 1300    | -               |
| GitHub Actions | 2000    | 500MB           |

 
We don't expect to be be releasing packages any time soon, 
which means the last column is not as important as the rest. 
In this scenario, GitHub Actions will be the best of the bunch
with 2000 minutes per month.


## Final choice

The last three options meet all of our the requirements. GitHub 
action has a few perks: more minutes and better GitHub integration.
However, when investigating the feature set of the tools themselves 
(not the plans) I found GitLab CI/CD has the most variety and has 
also been around for longer, which according to some articles led
to a more mature design overall. Semaphore CI was somewhat in the 
middle, with not as many perfected features but a reasonable set
nonetheless. And lastly, GitHub Actions seemed simpler overall.

Considering all of this, we decided to try GitHub Actions and 
GitLab CI/CD as our CI tools. GitHub Actions will be a straightfoward
way of testing CI as is already integrated and we are already
familiar with it. On top of that, it offers 2000 minutes a month.
GitLab CI/CD, on the other hand, might provide a more solid
environment that allows for more features and options.
