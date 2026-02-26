# When the Numbers Don't Match
**Quick Guide to Resource Verification in Flow**

---

## The Problem (In Plain Language)

You're in Node A. You sent 10,000 kg of grain to Node B.  
But Node B says they only received 8,000 kg.

Where did 2,000 kg go?

**Possible reasons:**
- Someone's scale is broken
- Some grain spoiled in the truck
- Someone wrote down the wrong number
- The containers leaked
- (Rarely) Someone took it

**The challenge:** Figure out what happened without:
- Spying on people
- Assuming someone is lying
- Breaking trust
- Creating a surveillance system

---

## How It Works (The Simple Version)

### Step 1: Check Your Own Stuff (1 week)

Both nodes look at their own process:
- Is our scale working?
- Did we write it down correctly?
- Did anything spoil in storage?
- Are our containers the right size?

**Most issues get solved here.** "Oh, our scale was off by 12%!"

### Step 2: Watch One Delivery Together (2 weeks)

If Step 1 doesn't solve it, a neutral team (from other nodes) watches one full delivery:
- They watch loading at Node A
- They ride along in the truck
- They watch unloading at Node B
- They measure at each step

**Goal:** Find where the loss happens. Usually it's something technical like:
- Grain settling during transport (looks like more at start, less at end)
- Leaky containers
- Measurement differences (one node measures by volume, other by weight)

### Step 3: Fix the Cause

Once you know what's happening, fix it:
- **Technical problem?** Get better equipment
- **Process mistake?** Update how you do things
- **Spoilage?** Use better containers or faster transport
- **Still can't explain it?** See the next section

---

## What If Someone Is Actually Stealing?

**First: We assume people are good.** Most problems are honest mistakes.

But if you find actual evidence of intentional theft, there's a ladder of responses:

### Level 1: Talk About It Openly
The investigation team shares what they found with both nodes and the wider network.  
If the node accepts it and fixes things → great, problem solved.

### Level 2: Witnessed Deliveries (6 months)
For the next 6 months, every delivery from that node is watched by a neutral observer.
- If problems stop → it really was just a technical issue
- If problems continue → go to Level 3

### Level 3: Limited Trading
That node can only trade with nodes that specifically agree to work with them.  
Other nodes reduce their dependency on that node.  
Lasts until the node shows 6 months of accurate trading.

### Level 4: Exit from Regional Network
If a node refuses to investigate or keeps diverting resources, they exit the regional resource-sharing system.

**Important:** Individual people from that node still have Baseline access through other means. This is about the node as an organization, not punishing people.

---

## Protection Against False Accusations

You can't just accuse another node of stealing. You need:
- **Multiple data points** (not just one incident)
- **Physical evidence** (not just "I think they did it")
- **A pattern over time** (minimum 3 months)
- **Ruled out all other explanations** (technical, environmental, etc.)

**And if someone makes a false accusation on purpose?**  
They get treated the same way as if they had stolen resources. Weaponizing verification is just as bad as theft.

---

## Prevention: Stop Problems Before They Start

**Better tools:**
- Calibrated scales at exchange hubs
- Standardized containers (so everyone knows the size)
- Regular equipment checks

**Better processes:**
- Log things the moment they happen (not later)
- Transport gets documented too (who's carrying it, when it should arrive)
- Nodes pair up as "witness partners" and double-check each other

**Better culture:**
- Admitting a mistake early is good, not shameful
- Every solved problem becomes a lesson for everyone else
- "Our storage barrels were leaking 8% over 3 weeks" → now everyone checks their barrels

---

## The Philosophy

**We verify** because:
- People's lives depend on accurate resource tracking
- Small errors add up
- Baseline security requires knowing what we actually have

**We verify gently** because:
- Most discrepancies are honest mistakes
- Surveillance destroys the trust we're trying to protect
- Flow works through transparency, not policing

**Trust is earned through transparency.**  
**Verification is care, not suspicion.**  
**Discrepancies are signals, not sins.**

---

## Quick Visual: The Process

```
Numbers don't match
        ↓
Yellow flag: "Heads up, check this"
        ↓
Step 1: Both sides check their own process (1 week)
        ↓
Solved? → YES: Document the lesson, move on
        ↓ NO
Step 2: Neutral team watches one delivery (2 weeks)
        ↓
Found the cause? → YES: Fix it (equipment/process/storage)
        ↓ NO (very rare)
Step 3: Is it intentional diversion?
        ↓
YES: Start the response ladder (Levels 1-4)
NO: Keep investigating
```

---

## Success Looks Like This

- 90%+ of issues solved in Step 1 (self-check)
- Less than 5% need the response ladder
- Less than 1% reach exclusion
- Average resolution time: under a month

---

## Want More Details?

See **FLOW_VERIFICATION_REFERENCE.md** for:
- Exact timelines for each step
- Detailed evidence requirements
- Integration with other protocols
- Metrics and accountability measures
- Cultural considerations
- Edge cases and special scenarios

---

**Remember:** This protocol exists to protect everyone's Baseline while maintaining trust. We count carefully because lives depend on it. But we count gently because trust is a resource too.

---

**Status:** Quick Guide  
**For:** Anyone who needs to understand the basics  
**Next Steps:** If you're implementing this, read the Reference Guide

